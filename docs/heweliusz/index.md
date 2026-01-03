# Jan Heweliusz Disaster Analysis

*Project: November 2025*

**Role:** Data Scientist

---

## Project description

<div style="text-align: justify;">
The disaster of the ferry <strong>MS Jan Heweliusz</strong> (January 14, 1993) was analyzed for years mainly in a descriptive manner, without full reconstruction of meteorological conditions and their impact on vessel stability.

This project aimed to <strong>reconstruct the course of the disaster in a data-driven way, based on physics and validatable models</strong>.

I conducted a <strong>comprehensive meteorological-technical analysis</strong> combining:

- ERA5 meteorological reanalyses (ECMWF),
- CMEMS wave data,
- hydrodynamics and stability laws,
- official commission reports and court rulings.
</div>

---

## Analysis Scope

### 1. Meteorological Conditions

- atmospheric pressure (MSLP)
- wind speed and direction
- wave height and energy
- barometric gradient analysis

### 2. Storm Dynamics

- identification of **explosive cyclogenesis** (Bergeron criterion: ≥20 hPa / 24h)
- rapid escalation of conditions in hours preceding the disaster

### 3. Hydrodynamics and Stability

- **Beam Sea** wave analysis
- **parametric rolling** mechanism
- escalation of heeling leading to loss of stability

### 4. Data Validation

- ERA5 vs CMEMS comparison
- correlation, RMSE, bias
- reconstruction reliability assessment

---

## Key Findings

### Weather Conditions
- Pressure drop of **27 hPa in < 24h**
- Wind up to **24.2 m/s (9°B – severe gale)**
- Wave energy increased nearly **5× in 6 hours**

### Hydrodynamics
- Waves hit the hull at ~**60°** angle
- Maximum wind force on hull: **~393 kN**
- Vessel remained in **Beam Sea** zone
- Heel resonance (parametric rolling)

### Heel Escalation
- 0° → 35° in 5h 40min
- 35° → 90° in **36 minutes**

### Validation
- ERA5 vs CMEMS: **r = 0.982**
- R² = **0.964**
- Energy differences result from non-linearity (E ∝ H²), not data errors

---

## What I did

- Acquired and processed ERA5 and CMEMS data
- Performed temporal and spatial analyses
- Calculated wave energy and forces acting on the vessel
- Built visualizations of correlation and phenomenon escalation
- Compared scientific data with commission findings
- Developed coherent narrative based on data and physics

---

## Skills

- Python
- Pandas
- NumPy
- xarray
- ERA5 (ECMWF)
- CMEMS (Copernicus Marine)
- Scientific Visualization
- Data Validation

---

## Results

- Quantitative reconstruction of disaster mechanism
- Confirmation of convergence of extreme weather phenomena and technical-operational errors
- High analysis reliability through source validation
- Example of Data Science application to historical event analysis

---

## Conclusions

<div style="text-align: justify;">
The MS <em>Jan Heweliusz</em> disaster was a <strong>systemic culmination</strong> of:

- severe storm (9°B),
- beam sea waves,
- rapid cyclogenesis,
- improper vessel preparation for the voyage.

The project demonstrates how <strong>data analysis, physics, and model validation</strong> enable understanding complex events in an objective and replicable way.
</div>

---

## Sample photos

![Beam Sea Analysis](data/beam_sea_analysis.png)
![Energy and Force](data/energy_and_force.png)
![Multi Parameter Analysis](data/multi_parameter_analysis.png)
![Ship Heel](data/ship_heel.png)
![Spatial Conditions](data/spatial_conditions.png)
![Wind Wave Rose](data/wind_wave_rose.png)

