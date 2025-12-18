# Spinning ball spiral
# ⚽ In Search of the Perfect Free-Kick
### An Experimental Investigation of the Magnus Effect and Trajectory Spirals

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![LaTeX](https://img.shields.io/badge/LaTeX-Paper-green)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

## 📖 Abstract

This project investigates the aerodynamics of spinning spherical projectiles, inspired by the legendary "perfect free-kick" scored by Roberto Carlos in 1997. 

By transposing the problem to a laboratory scale (marbles in water and oil), we analyze the **Magnus effect** and the transition from circular trajectories to **"Spinning Ball Spirals"** (as described by C. Clanet). This repository contains the experimental data analysis code (Python) and the full research paper (LaTeX).

## 📂 Repository Structure

* `magnus_analysis.py`: Main Python script for trajectory reconstruction, velocity analysis, and regression plotting.
* `main.tex`: The complete scientific paper written in LaTeX.
* `huile.xlsx`: Experimental data (position tracking) obtained in viscous fluid (oil).
* `images/`: Contains diagrams and plots used in the paper.

## 🚀 Key Features

* **Trajectory Reconstruction:** Uses high-speed chronophotography data to reconstruct the path of the projectile using a **discrete summation assumption** ($\sum \Delta s$) for high precision.
* **Physics Modeling:** Validates the exponential decay of velocity: $U(s) = U_0 e^{-s/\delta}$.
* **Uncertainty Analysis:** Includes full error propagation (Z-score calculation) to validate the theoretical model against experimental data.
* **Reynolds Number Comparison:** Compares turbulent regimes in water ($Re \approx 10^5$) vs. oil ($Re \approx 10^3$).

## 🛠️ Installation & Usage

### Prerequisites
You need **Python** installed with the following scientific libraries:

```bash
pip install numpy pandas matplotlib openpyxl
```
## Running the Analysis
To generate the regression plots and Z-score graphs:
```Bash
python magnus_analysis.py
```

## 📊 Results Preview
The Python script generates two main visualizations:  
Linear Regression: $\ln(U)$ vs. Curvilinear Abscissa $s$.  
This validates the drag coefficient $C_x$.Z-Score Evolution: Demonstrates that experimental deviations remain within statistical uncertainty boundaries ($Z < 2$). 
## 📚 References  
This work relies on the foundational research of:
- Christophe Clanet et al. (The spinning ball spiral, 2010)
- Dupeux, Cohen, Le Goff, Quéré (Le Football et ses trajectoires, 2012)
- Bray & Kerwin (Modelling the flight of a soccer ball, 2003)
👤 Author : Théo Palagi Academic Project (TIPE) - SCEI n° 44821 Session 2023-2024
