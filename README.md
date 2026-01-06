# Monte Carlo Simulation of Rock Climbing Fatigue

## Overview

This project models **rock climbing fatigue** and the probability of successfully completing a climbing route using **Monte Carlo simulations**.  
By combining a Python-based climbing simulator with MATLAB visualizations, we estimate climber fatigue under different conditions and analyze success probabilities.

The simulation considers:  
- Climber attributes: strength, endurance, and technique.  
- Route features: different hold types and rest points.  
- Randomness in fatigue accumulation to reflect real-world variability.  

---

## Methods

### Python Simulation

The `AscentSimulator` class in Python computes cumulative fatigue as a climber progresses along a route. Fatigue is influenced by:  
- The type of hold (jug, crimp, sloper, etc.)  
- The climber's strength and endurance  
- Random variation to model uncertainty  

Monte Carlo simulation is used to run multiple trials and estimate:  
- Average, minimum, and maximum fatigue  
- Probability of successfully completing the climb  

### MATLAB Visualization

The fatigue results are passed to MATLAB via the MATLAB Engine API.  
A **line graph** visualizes fatigue across Monte Carlo trials for better trend analysis.

---

## Results

Example output from 100 Monte Carlo trials:

Monte Carlo Results (100 trials):
Average fatigue: 17.22
Minimum fatigue: 3.11
Maximum fatigue: 32.64
Success probability: 59.00%


**Line graph of fatigue across trials:**  

![Line Graph of Climbing Fatigue](path/to/your/screenshot.png)

---

## Analysis

- The success probability (50–70%) is realistic given the randomness introduced in fatigue.  
- Fatigue varies significantly between trials, demonstrating how small changes in grip difficulty or climber strength can impact performance.  
- The simulation framework can be extended to test different routes, climber profiles, or fatigue models.

---

## How to Run

### Python Environment

# Create and activate environment
conda create -n climbing python=3.13
conda activate climbing

# Install dependencies
pip install numpy matlab.engine

Run Simulation
# From the project root
python Experiments/test_climb.py 

MATLAB
- MATLAB must be installed (tested with R2025b).
- The Python script automatically passes results to MATLAB for plotting.


## Future Improvements
- Incorporate additional climber attributes (e.g., flexibility, grip endurance).
- Add more detailed rest mechanics and recovery modeling.
- Extend visualization to include success/failure probabilities per hold.

## Project Structure

```bash
Rock_Climbing_Project/
├── src/
│   ├── climbing_sim.py
│   └── ascent_simulator.py
├── Experiments/
│   └── test_climb.py
├── README.md
└── screenshots/
    └── fatigue_line_graph.png

