import sys
import os
import numpy as np
from contextlib import redirect_stdout
import io

src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src'))
sys.path.insert(0, src_path)

from climbing_sim import Hold, Route, Climber, FatigueModel
from ascent_simulator import AscentSimulator

holds = [
    Hold("jug", 0.5, 0.2),
    Hold("crimp", 1.0, 0.5),
    Hold("sloper", 1.2, 0.7),
    Hold("pinch", 0.8, 0.6),
    Hold("pocket", 1.0, 0.5),
    Hold("undercling", 1.3, 0.8),
    Hold("gaston", 1.1, 0.6)
]

route = Route(holds, rest_indices=[1, 4])
climber = Climber(strength=5.0, endurance=4.0, technique=1.5)
fatigue_model = FatigueModel(noise_std=2.0, scale=3.0)
simulator = AscentSimulator(climber, route, fatigue_model)

# Single ascent
simulator.simulate_ascent()

# Monte Carlo simulation
n_trials = 100
simulator.monte_carlo(n_trials)
