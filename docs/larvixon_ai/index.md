# Larvixon-AI

*Project start: April 2025 — Present*

**Role:** AI / Computer Vision Engineer

**Collaboration:** Medical University of Wrocław

---

## Project description

**Larvixon-AI** is a system based on **computer vision and deep learning** that automatically analyzes movement behaviors of **Galleria mellonella** larvae after injection of selected bacterial pathogens.

Sepsis is one of the most serious problems in modern medicine, and rapid pathogen identification is crucial for implementing appropriate therapy. Classic diagnostic methods:

- are time-consuming (24–72 hours),
- require advanced laboratory facilities,
- don't always allow for quick clinical decisions.

The **Galleria mellonella** model enables observation of behavioral changes after infection. However, previous analysis was manual, difficult to standardize, and limited in scalability.

The project is carried out as a **master's thesis** in collaboration with the **Medical University of Wrocław**.

---

## How It Works

Larvixon-AI is a video analysis pipeline:

- **Video ingestion** — HD recordings (25 FPS), various lighting conditions
- **Computer Vision layer** — object detection (larvae), segmentation and masking, position tracking across frames
- **Analysis layer** — trajectory calculation, distance, speed, directions, activity heat maps
- **Data & visualization** — CSV export, statistical analysis, result visualizations

The architecture is prepared for further integration with deep learning models.

---

## What I did

- Designed the algorithm for larvae detection and tracking in video
- Implemented image processing pipeline in OpenCV
- Handled different lighting variants (top / bottom)
- Calculated trajectories and kinematic movement parameters
- Conducted comparative analysis of groups:
    - control
    - PBS
    - *E. coli* infected (various concentrations)
- Automated data export and visualization generation
- Analyzed results for behavioral differences

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

Larvixon-AI provides a foundation for further research on:

- automatic identification of septic pathogens,
- accelerating infection diagnostics,
- using deep learning in behavioral analysis.

The project connects **AI engineering** with **biomedical research** and bridges science with practical clinical applications.

---

## Sample photos

![Recording setup](data/recording.png)
![Preprocessing](data/preprocessing.png)
![Trajectory analysis 1](data/trajectory-1.png)
![Trajectory analysis 2](data/trajectory-2.png)
![Speed analysis](data/speed.png)
![Heatmaps](data/heatmaps.png)
![Rose diagram](data/rose.png)
![Bubble chart](data/bubble.png)
