# AI-Based Space Debris Avoidance System

## Overview
This project is an educational simulation of an AI-based space debris avoidance system designed for low Earth orbit operations. It integrates real Two-Line Element (TLE) data to track satellites and orbital debris, evaluates collision risk using a machine-learning model, and applies autonomous, fuel-aware avoidance maneuvers.

## Problem Statement
Orbital debris poses a significant threat to active satellites. Even small objects can cause catastrophic damage due to high relative velocities. Autonomous collision avoidance systems are essential to improve satellite safety and mission longevity.

## System Architecture
The system follows a modular aerospace-style architecture:
- TLE-based orbit data ingestion
- Relative position and velocity sensing
- AI-based collision risk estimation
- Autonomous maneuver decision logic
- Mission control graphical interface

## Key Components
- **AI Decision Module**: Estimates collision probability based on distance and closing velocity.
- **Sensor Module**: Computes relative navigation parameters between satellite and debris.
- **Maneuver Module**: Executes fuel-aware altitude adjustment strategies.
- **TLE Loader**: Fetches real satellite and debris data from CelesTrak.
- **GUI**: Displays system status and risk assessment in real time.

## Technologies Used
- Python
- NumPy
- scikit-learn
- Skyfield
- Tkinter

## Data Sources
- CelesTrak Two-Line Element (TLE) datasets for active satellites and orbital debris

## Purpose
This project is intended for educational and research demonstration purposes, illustrating key concepts in space situational awareness, autonomous decision-making, and orbital safety systems.

## Future Improvements
- Reinforcement learning–based maneuver optimization
- 3D orbit visualization
- Integration of additional debris catalogs
- Fuel consumption modeling

## Disclaimer
This project is a simulation and does not represent an operational flight system.