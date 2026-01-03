# Robinson Chatbot

*Start projektu: 2025-01-31*

## Opis projektu

Projekt Robinson Chatbot eksploruje implementację technik **Retrieval-Augmented Generation (RAG)** do stworzenia inteligentnego agenta konwersacyjnego posiadającego wiedzę o "Robinsonie Crusoe". System łączy najnowocześniejsze modele językowe zarówno od **OpenAI**, jak i **Amazon Bedrock** z zaawansowanymi metodami wyszukiwania tekstu, aby zapewnić dokładne, kontekstowo istotne odpowiedzi oparte na treści powieści. Poprzez intensywne eksperymenty z **różnymi strategiami chunkingu, modelami embeddingów i technikami prompt engineering**, projekt demonstruje jak architektury RAG mogą skutecznie rozszerzać możliwości LLM dla aplikacji domenowych, jednocześnie minimalizując halucynacje i poprawiając dokładność faktyczną.

## Główne funkcjonalności

- Implementacja **różnych metod chunkingu tekstu** (np. po paragrafach, stały rozmiar tokenów, po rozdziałach) do optymalizacji wyszukiwania informacji
- Eksperymenty z różnymi modelami embeddingów do tworzenia semantycznych reprezentacji wektorowych
- Zaawansowane wyszukiwanie podobieństwa przy użyciu **bazy wektorowej FAISS** dla efektywnego wyszukiwania informacji
- Porównanie wydajności między modelami OpenAI (**gpt-4o** i **gpt-4o-mini**) a modelami Amazon Bedrock (**Amazon Titan Text Express V1** i **Amazon Titan Text Embeddings E1**)
- **Techniki prompt engineering** do optymalizacji wykorzystania kontekstu i jakości odpowiedzi
- Interaktywna **aplikacja Streamlit** do przyjaznej użytkownikowi interakcji z chatbotem o Robinsonie Crusoe
- Kompleksowy framework ewaluacyjny do mierzenia dokładności, trafności i spójności odpowiedzi

## Umiejętności

- Python
- OpenAI
- Amazon Bedrock
- AWS
- NumPy
- FAISS
- RAG
- Boto3
- NLTK
- Streamlit
- Prompt Engineering
- Embeddings
- LaTeX

## Raport projektu

**Możesz pobrać** i przejrzeć kompletny raport projektu ze szczegółową metodologią i wynikami tutaj:
[Robinson Chatbot - Raport implementacji RAG](Project_RAG.pdf)

## Zdjęcia

![Chunking](../robinson_chatbot/data/chunking.png)
![Prompty](../robinson_chatbot/data/prompts.png)
![Rozmowa](../robinson_chatbot/data/conversation.png)
![Gotowe prompty](../robinson_chatbot/data/ready_prompts.png)
![Modele](../robinson_chatbot/data/models.png)

