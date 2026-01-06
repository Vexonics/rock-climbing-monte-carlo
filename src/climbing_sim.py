import numpy as np

class Hold:
    def __init__(self, grip_type, difficulty, length):
        self.grip_type = grip_type
        self.difficulty = difficulty
        self.length = length

class Route:
    def __init__(self, holds, rest_indices=None):
        self.holds = holds
        self.rest_indices = rest_indices or []

class Climber:
    def __init__(self, strength, endurance, technique):
        self.strength = strength
        self.endurance = endurance
        self.technique = technique

class FatigueModel:
    def __init__(self, noise_std=0.05, scale=1.0):
        self.noise_std = noise_std
        self.scale = scale

    def fatigue_cost(self, climber, hold):
        base = hold.difficulty * (1.0 / climber.strength + 1.0 / climber.endurance)
        noise = np.random.normal(0, self.noise_std)
        return max(base + noise, 0) * self.scale
