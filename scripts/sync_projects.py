#!/usr/bin/env python3
"""
Skrypt synchronizujący projekty z Obsidian Vault do Portfolio MkDocs.
Obsługuje dwujęzyczne treści (EN/PL).

Użycie:
    python scripts/sync_projects.py --vault-path /ścieżka/do/vault/Projects

Funkcjonalności:
    - Parsuje frontmatter YAML z notatek Obsidian
    - Waliduje strukturę danych projektu
    - Kopiuje zdjęcia z vault do portfolio
    - Generuje strony w języku angielskim i polskim
    - Generuje projects.json z metadanymi
    - Tworzy changelog zmian
"""

import os
import sys
import json
import yaml
import re
import shutil
from pathlib import Path
from datetime import datetime
from dataclasses import dataclass, asdict, field
from typing import Optional, List, Dict
import argparse


@dataclass
class ProjectMetadata:
    """Struktura metadanych projektu - walidacja i standaryzacja."""
    id: str
    title: str
    title_pl: str = ""
    role: str = "Data Scientist"
    status: str = "completed"
    tags: list = field(default_factory=list)
    date_from: str = ""
    date_to: str = ""
    stack: list = field(default_factory=list)
    repo: str = ""
    demo: str = ""
    highlights: list = field(default_factory=list)
    highlights_pl: list = field(default_factory=list)
    metrics: dict = field(default_factory=dict)
    featured: bool = False
    order: int = 999
    images: dict = field(default_factory=dict)

    def validate(self) -> list:
        """Walidacja metadanych - zwraca listę błędów."""
        errors = []
        if not self.id:
            errors.append("Brak 'id' projektu")
        if not self.title:
            errors.append("Brak 'title' projektu")
        if self.status not in ["draft", "in_progress", "completed", "production"]:
            errors.append(f"Nieprawidłowy status: {self.status}")
        return errors


@dataclass
class ProjectContent:
    """Zawartość projektu - sekcje markdown (EN i PL)."""
    problem: str = ""
    problem_pl: str = ""
    solution: str = ""
    solution_pl: str = ""
    what_i_did: str = ""
    what_i_did_pl: str = ""
    results: str = ""
    results_pl: str = ""
    raw_content: str = ""


def parse_frontmatter(content: str) -> tuple[dict, str]:
    """Parsuje frontmatter YAML z pliku markdown."""
    pattern = r'^---\s*\n(.*?)\n---\s*\n(.*)$'
    match = re.match(pattern, content, re.DOTALL)
    
    if not match:
        return {}, content
    
    try:
        frontmatter = yaml.safe_load(match.group(1))
        body = match.group(2)
        return frontmatter or {}, body
    except yaml.YAMLError as e:
        print(f"Błąd parsowania YAML: {e}")
        return {}, content


def parse_sections(body: str) -> ProjectContent:
    """Parsuje sekcje markdown na strukturę ProjectContent (EN i PL)."""
    content = ProjectContent(raw_content=body)
    
    # Wzorce dla sekcji (EN)
    section_patterns_en = {
        'problem': r'##\s*Problem\s*\n(.*?)(?=##|\Z)',
        'solution': r'##\s*Solution\s*\n(.*?)(?=##|\Z)',
        'what_i_did': r'##\s*What I did\s*\n(.*?)(?=##|\Z)',
        'results': r'##\s*Results\s*\n(.*?)(?=##|\Z)',
    }
    
    # Wzorce dla sekcji (PL)
    section_patterns_pl = {
        'problem_pl': r'##\s*Problem_PL\s*\n(.*?)(?=##|\Z)',
        'solution_pl': r'##\s*Solution_PL\s*\n(.*?)(?=##|\Z)',
        'what_i_did_pl': r'##\s*What I did_PL\s*\n(.*?)(?=##|\Z)',
        'results_pl': r'##\s*Results_PL\s*\n(.*?)(?=##|\Z)',
    }
    
    # Parsuj EN
    for key, pattern in section_patterns_en.items():
        match = re.search(pattern, body, re.DOTALL | re.IGNORECASE)
        if match:
            setattr(content, key, match.group(1).strip())
    
    # Parsuj PL
    for key, pattern in section_patterns_pl.items():
        match = re.search(pattern, body, re.DOTALL | re.IGNORECASE)
        if match:
            setattr(content, key, match.group(1).strip())
    
    return content


def copy_images(vault_path: Path, output_path: Path, project_id: str, 
                images_config: dict, dry_run: bool = False) -> dict:
    """Kopiuje zdjęcia z vault do folderu projektu w portfolio."""
    copied_images = {
        'cover': '',
        'architecture': '',
        'gallery': []
    }
    
    if not images_config:
        return copied_images
    
    images_dir = output_path / project_id / 'images'
    
    def copy_single_image(relative_path: str) -> str:
        if not relative_path:
            return ''
        
        source_path = vault_path / relative_path
        
        if not source_path.exists():
            print(f"      ⚠️  Nie znaleziono: {relative_path}")
            return ''
        
        filename = source_path.name
        dest_path = images_dir / filename
        
        if not dry_run:
            images_dir.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source_path, dest_path)
            print(f"      📷 Skopiowano: {filename}")
        else:
            print(f"      📷 [DRY RUN] Skopiowałbym: {filename}")
        
        return f"images/{filename}"
    
    if 'cover' in images_config and images_config['cover']:
        copied_images['cover'] = copy_single_image(images_config['cover'])
    
    if 'architecture' in images_config and images_config['architecture']:
        copied_images['architecture'] = copy_single_image(images_config['architecture'])
    
    if 'gallery' in images_config and images_config['gallery']:
        for item in images_config['gallery']:
            if isinstance(item, dict) and 'path' in item:
                new_path = copy_single_image(item['path'])
                if new_path:
                    copied_images['gallery'].append({
                        'path': new_path,
                        'caption': item.get('caption', ''),
                        'caption_pl': item.get('caption_pl', item.get('caption', ''))
                    })
            elif isinstance(item, str):
                new_path = copy_single_image(item)
                if new_path:
                    copied_images['gallery'].append({
                        'path': new_path,
                        'caption': '',
                        'caption_pl': ''
                    })
    
    return copied_images


def load_project_from_obsidian(file_path: Path) -> tuple[ProjectMetadata, ProjectContent]:
    """Ładuje projekt z pliku Obsidian."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    frontmatter, body = parse_frontmatter(content)
    
    metadata = ProjectMetadata(
        id=frontmatter.get('id', file_path.stem),
        title=frontmatter.get('title', file_path.stem.replace('_', ' ').title()),
        title_pl=frontmatter.get('title_pl', frontmatter.get('title', '')),
        role=frontmatter.get('role', 'Data Scientist'),
        status=frontmatter.get('status', 'completed'),
        tags=frontmatter.get('tags', []),
        date_from=str(frontmatter.get('date_from', '')),
        date_to=str(frontmatter.get('date_to', '')),
        stack=frontmatter.get('stack', []),
        repo=frontmatter.get('repo', ''),
        demo=frontmatter.get('demo', ''),
        highlights=frontmatter.get('highlights', []),
        highlights_pl=frontmatter.get('highlights_pl', frontmatter.get('highlights', [])),
        metrics=frontmatter.get('metrics', {}),
        featured=frontmatter.get('featured', False),
        order=frontmatter.get('order', 999),
        images=frontmatter.get('images', {}),
    )
    
    project_content = parse_sections(body)
    
    return metadata, project_content


def generate_mkdocs_page(metadata: ProjectMetadata, content: ProjectContent, 
                         images: dict, lang: str = 'en') -> str:
    """Generuje stronę MkDocs z metadanych, zawartości i zdjęć."""
    
    # Wybierz odpowiedni tytuł i treści
    title = metadata.title if lang == 'en' else (metadata.title_pl or metadata.title)
    highlights = metadata.highlights if lang == 'en' else (metadata.highlights_pl or metadata.highlights)
    
    problem = content.problem if lang == 'en' else (content.problem_pl or content.problem)
    solution = content.solution if lang == 'en' else (content.solution_pl or content.solution)
    what_i_did = content.what_i_did if lang == 'en' else (content.what_i_did_pl or content.what_i_did)
    results = content.results if lang == 'en' else (content.results_pl or content.results)
    
    # Etykiety
    labels = {
        'en': {
            'technologies': 'Technologies',
            'highlights': '✨ Key Achievements',
            'metrics': '📊 Metrics',
            'metric': 'Metric',
            'value': 'Value',
            'stack': '🛠️ Tech Stack',
            'architecture': '🏗️ Architecture',
            'problem': '🎯 Problem',
            'solution': '💡 Solution',
            'what_i_did': '👨‍💻 What I Did',
            'results': '📈 Results',
            'gallery': '📸 Gallery',
            'repo': '📂 Repository',
            'demo': '🌐 Demo',
        },
        'pl': {
            'technologies': 'Technologie',
            'highlights': '✨ Kluczowe osiągnięcia',
            'metrics': '📊 Metryki',
            'metric': 'Metryka',
            'value': 'Wartość',
            'stack': '🛠️ Stack technologiczny',
            'architecture': '🏗️ Architektura',
            'problem': '🎯 Problem',
            'solution': '💡 Rozwiązanie',
            'what_i_did': '👨‍💻 Co zrobiłem',
            'results': '📈 Rezultaty',
            'gallery': '📸 Galeria',
            'repo': '📂 Repozytorium',
            'demo': '🌐 Demo',
        }
    }
    L = labels[lang]
    
    # Nagłówek
    page = f"# {title}\n\n"
    
    # Cover image - dla PL użyj ścieżki względnej do głównego folderu projektu
    if images.get('cover'):
        img_path = images['cover'] if lang == 'en' else f"../{metadata.id}/{images['cover']}"
        page += f"![{title}]({img_path})\n\n"
    
    # Tagi
    if metadata.tags:
        page += f"**{L['technologies']}:** "
        page += " · ".join([f"`{tag}`" for tag in metadata.tags])
        page += "\n\n"
    
    # Info
    info_items = []
    if metadata.date_from:
        date_range = metadata.date_from
        if metadata.date_to:
            date_range += f" – {metadata.date_to}"
        info_items.append(f"📅 {date_range}")
    if metadata.status:
        status_emoji = {'draft': '📝', 'in_progress': '🔄', 'completed': '✅', 'production': '🚀'}
        info_items.append(f"{status_emoji.get(metadata.status, '📌')} {metadata.status.replace('_', ' ').title()}")
    if metadata.role:
        info_items.append(f"👤 {metadata.role}")
    
    if info_items:
        page += " | ".join(info_items) + "\n\n"
    
    # Linki
    if metadata.repo or metadata.demo:
        links = []
        if metadata.repo:
            links.append(f"[{L['repo']}]({metadata.repo})")
        if metadata.demo:
            links.append(f"[{L['demo']}]({metadata.demo})")
        page += " · ".join(links) + "\n\n"
    
    # Highlights
    if highlights:
        page += f"## {L['highlights']}\n\n"
        for highlight in highlights:
            page += f"- {highlight}\n"
        page += "\n"
    
    # Metryki
    if metadata.metrics:
        page += f"## {L['metrics']}\n\n"
        page += f"| {L['metric']} | {L['value']} |\n|---------|--------|\n"
        for key, value in metadata.metrics.items():
            page += f"| {key.replace('_', ' ').title()} | {value} |\n"
        page += "\n"
    
    # Stack
    if metadata.stack:
        page += f"## {L['stack']}\n\n"
        page += " · ".join([f"`{tech}`" for tech in metadata.stack])
        page += "\n\n"
    
    # Architektura
    if images.get('architecture'):
        img_path = images['architecture'] if lang == 'en' else f"../{metadata.id}/{images['architecture']}"
        page += f"## {L['architecture']}\n\n"
        page += f"![{L['architecture']}]({img_path})\n\n"
    
    # Sekcje
    if problem:
        page += f"## {L['problem']}\n\n"
        page += f"<div style=\"text-align: justify;\">\n{problem}\n</div>\n\n"
    
    if solution:
        page += f"## {L['solution']}\n\n"
        page += f"<div style=\"text-align: justify;\">\n{solution}\n</div>\n\n"
    
    if what_i_did:
        page += f"## {L['what_i_did']}\n\n"
        page += f"<div style=\"text-align: justify;\">\n{what_i_did}\n</div>\n\n"
    
    if results:
        page += f"## {L['results']}\n\n"
        page += f"<div style=\"text-align: justify;\">\n{results}\n</div>\n\n"
    
    # Galeria
    if images.get('gallery'):
        page += f"## {L['gallery']}\n\n"
        for img in images['gallery']:
            caption = img.get('caption', '') if lang == 'en' else img.get('caption_pl', img.get('caption', ''))
            img_path = img['path'] if lang == 'en' else f"../{metadata.id}/{img['path']}"
            page += f"![{caption}]({img_path})\n"
            if caption:
                page += f"*{caption}*\n"
            page += "\n"
    
    # Fallback
    if not any([problem, solution, what_i_did, results]):
        if content.raw_content:
            page += content.raw_content
    
    return page


def sync_projects(vault_path: Path, output_path: Path, dry_run: bool = False) -> dict:
    """Główna funkcja synchronizacji."""
    results = {
        'synced': [],
        'errors': [],
        'skipped': [],
        'images_copied': 0,
        'timestamp': datetime.now().isoformat()
    }
    
    projects_data = []
    md_files = list(vault_path.glob('*.md'))
    
    if not md_files:
        print(f"⚠️  Nie znaleziono plików .md w: {vault_path}")
        return results
    
    print(f"📂 Znaleziono {len(md_files)} plików projektów\n")
    
    # Utwórz folder pl jeśli nie istnieje
    pl_folder = output_path / 'pl'
    if not dry_run:
        pl_folder.mkdir(parents=True, exist_ok=True)
    
    for md_file in md_files:
        print(f"📄 Przetwarzam: {md_file.name}")
        
        try:
            metadata, content = load_project_from_obsidian(md_file)
            
            errors = metadata.validate()
            if errors:
                results['errors'].append({'file': str(md_file), 'errors': errors})
                print(f"   ❌ Błędy walidacji: {errors}")
                continue
            
            # Kopiuj zdjęcia (tylko raz, do głównego folderu)
            copied_images = copy_images(
                vault_path, output_path, metadata.id, 
                metadata.images, dry_run
            )
            
            if copied_images.get('cover'):
                results['images_copied'] += 1
            if copied_images.get('architecture'):
                results['images_copied'] += 1
            results['images_copied'] += len(copied_images.get('gallery', []))
            
            # Generuj stronę EN
            page_content_en = generate_mkdocs_page(metadata, content, copied_images, 'en')
            project_dir_en = output_path / metadata.id
            project_file_en = project_dir_en / 'index.md'
            
            if not dry_run:
                project_dir_en.mkdir(parents=True, exist_ok=True)
                with open(project_file_en, 'w', encoding='utf-8') as f:
                    f.write(page_content_en)
            
            # Generuj stronę PL
            page_content_pl = generate_mkdocs_page(metadata, content, copied_images, 'pl')
            project_dir_pl = pl_folder / metadata.id
            project_file_pl = project_dir_pl / 'index.md'
            
            if not dry_run:
                project_dir_pl.mkdir(parents=True, exist_ok=True)
                with open(project_file_pl, 'w', encoding='utf-8') as f:
                    f.write(page_content_pl)
            
            results['synced'].append({
                'id': metadata.id,
                'title': metadata.title,
                'file_en': str(project_file_en),
                'file_pl': str(project_file_pl),
                'images': len(copied_images.get('gallery', [])) + 
                         (1 if copied_images.get('cover') else 0) +
                         (1 if copied_images.get('architecture') else 0)
            })
            
            # JSON (bez images i _pl fields)
            project_data = {
                'id': metadata.id,
                'title': metadata.title,
                'title_pl': metadata.title_pl,
                'role': metadata.role,
                'status': metadata.status,
                'tags': metadata.tags,
                'date_from': metadata.date_from,
                'date_to': metadata.date_to,
                'stack': metadata.stack,
                'repo': metadata.repo,
                'demo': metadata.demo,
                'highlights': metadata.highlights,
                'highlights_pl': metadata.highlights_pl,
                'metrics': metadata.metrics,
                'featured': metadata.featured,
                'order': metadata.order,
            }
            projects_data.append(project_data)
            
            print(f"   ✅ Zsynchronizowano: {metadata.title} (EN + PL)")
            
        except Exception as e:
            results['errors'].append({'file': str(md_file), 'errors': [str(e)]})
            print(f"   ❌ Błąd: {e}")
    
    # Zapisz projects.json
    if not dry_run and projects_data:
        projects_data.sort(key=lambda x: (x.get('order', 999), x.get('date_from', '')), reverse=True)
        
        data_dir = output_path.parent / 'data'
        data_dir.mkdir(parents=True, exist_ok=True)
        
        with open(data_dir / 'projects.json', 'w', encoding='utf-8') as f:
            json.dump(projects_data, f, indent=2, ensure_ascii=False)
        
        print(f"\n📊 Zapisano data/projects.json ({len(projects_data)} projektów)")
    
    # Podsumowanie
    print("\n" + "="*50)
    print("📋 PODSUMOWANIE SYNCHRONIZACJI")
    print("="*50)
    print(f"✅ Zsynchronizowano: {len(results['synced'])} (EN + PL)")
    print(f"📷 Skopiowano zdjęć: {results['images_copied']}")
    print(f"❌ Błędy: {len(results['errors'])}")
    print(f"⏭️  Pominięto: {len(results['skipped'])}")
    
    return results


def main():
    parser = argparse.ArgumentParser(
        description='Synchronizacja projektów z Obsidian do Portfolio MkDocs (EN + PL)'
    )
    parser.add_argument(
        '--vault-path', '-v',
        type=str,
        required=True,
        help='Ścieżka do folderu Projects w Obsidian Vault'
    )
    parser.add_argument(
        '--output-path', '-o',
        type=str,
        default='docs',
        help='Ścieżka do folderu docs w repozytorium (domyślnie: docs)'
    )
    parser.add_argument(
        '--dry-run', '-d',
        action='store_true',
        help='Tryb testowy - nie zapisuje plików'
    )
    
    args = parser.parse_args()
    
    vault_path = Path(args.vault_path).expanduser().resolve()
    output_path = Path(args.output_path).resolve()
    
    if not vault_path.exists():
        print(f"❌ Ścieżka vault nie istnieje: {vault_path}")
        sys.exit(1)
    
    print("🔄 Synchronizacja Portfolio z Obsidian (EN + PL)")
    print(f"   Vault: {vault_path}")
    print(f"   Output: {output_path}")
    print(f"   Dry run: {args.dry_run}")
    print()
    
    results = sync_projects(vault_path, output_path, args.dry_run)
    
    if not args.dry_run:
        log_file = output_path.parent / 'data' / 'sync_log.json'
        with open(log_file, 'w', encoding='utf-8') as f:
            json.dump(results, f, indent=2, ensure_ascii=False)


if __name__ == '__main__':
    main()
