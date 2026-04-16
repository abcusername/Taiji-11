# Binary Neutron Star Simulation with Einstein Toolkit and Lorene

## Overview

This repository presents the key files and final results of a binary neutron star (BNS) simulation project based on **Einstein Toolkit** and **Lorene**. The project was completed as part of a numerical relativity selection task, with emphasis on simulation setup, waveform extraction, visualization, and result organization.

The repository includes:

- the main simulation parameter file
- extracted waveform data for the target gravitational-wave modes
- a Python post-processing script
- final waveform figures
- representative simulation logs
- an evolution video

## Project Objective

The objective of this project is to:

- compile and use **Einstein Toolkit** and **Lorene**
- construct an equal-mass binary neutron star system
- set the component masses to **1.2 + 1.2 solar masses**
- use an initial separation of **45 km**
- adopt a **polytropic equation of state**
- evolve the system dynamically
- extract gravitational-wave signals in the following modes:
  - \( l = 2, m = 0 \)
  - \( l = 2, m = 2 \)
- produce waveform plots and an evolution video

## Repository Structure

```text
.
├── README.md
├── data/
│   ├── processed/
│   │   ├── l2_m0_psi4.txt
│   │   └── l2_m2_psi4.txt
│   └── waveforms/
│       ├── psi4_l2_m0_r100.asc
│       └── psi4_l2_m2_r100.asc
├── figures/
│   ├── psi4_comparison.png
│   ├── psi4_l2_m0.png
│   └── psi4_l2_m2.png
├── logs/
│   ├── run_bns45_mpi16.err
│   └── run_bns45_mpi16.out
├── media/
│   └── bns_evolution.mp4
├── params/
│   └── bns_45km.par
└── scripts/
    └── plot_psi4.py
