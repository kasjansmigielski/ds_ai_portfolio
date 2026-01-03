# Larvixon-AI

*Project start: April 2025 — Present*

**Role:** AI / Computer Vision Engineer

**Collaboration:** Medical University of Wrocław

---

## Project description

<div style="text-align: justify;">
<strong>Larvixon-AI</strong> is a system based on <strong>computer vision and deep learning</strong> that automatically analyzes movement behaviors of <strong>Galleria mellonella</strong> larvae after injection of selected bacterial pathogens.

Sepsis is one of the most serious problems in modern medicine, and rapid pathogen identification is crucial for implementing appropriate therapy. Classic diagnostic methods:

- are time-consuming (24–72 hours),
- require advanced laboratory facilities,
- don't always allow for quick clinical decisions.

The <strong>Galleria mellonella</strong> model enables observation of behavioral changes after infection. However, previous analysis was manual, difficult to standardize, and limited in scalability.

The project is carried out as a <strong>master's thesis</strong> in collaboration with the <strong>Medical University of Wrocław</strong>.
</div>

---

## How It Works

<div style="text-align: justify;">
Larvixon-AI is a video analysis pipeline:

- **Video ingestion** — HD recordings (25 FPS), various lighting conditions
- **Computer Vision layer** — object detection (larvae), segmentation and masking, position tracking across frames
- **Analysis layer** — trajectory calculation, distance, speed, directions, activity heat maps
- **Data & visualization** — CSV export, statistical analysis, result visualizations

The architecture is prepared for further integration with deep learning models.
</div>

---

## What I did

1. Designed the algorithm for larvae detection and tracking in video
2. Implemented image processing pipeline in OpenCV
3. Handled different lighting variants (top / bottom)
4. Calculated trajectories and kinematic movement parameters
5. Conducted comparative analysis of groups:
   - control
   - PBS
   - *E. coli* infected (various concentrations)
6. Automated data export and visualization generation
7. Analyzed results for behavioral differences

---

## Skills

- Python
- OpenCV
- Deep Learning
- Computer Vision
- NumPy
- Pandas
- Scientific Computing
- Video Processing

---

## Key Results

- **100% movement detection accuracy**
- Real-time video processing (**25 FPS**)
- Significant differences between groups:
  - control larvae: ~5 mm/s
  - infected larvae: ~2.3 mm/s (high concentrations)
- Clear differences in:
  - traveled distances
  - spatial activity distribution
  - movement patterns

---

## Impact & Future Work

<div style="text-align: justify;">
Larvixon-AI provides a foundation for further research on:

- automatic identification of septic pathogens,
- accelerating infection diagnostics,
- using deep learning in behavioral analysis.

The project connects <strong>AI engineering</strong> with <strong>biomedical research</strong> and bridges science with practical clinical applications.
</div>

