import numpy as np

class AscentSimulator:
    def __init__(self, climber, route, fatigue_model):
        self.climber = climber
        self.route = route
        self.fatigue_model = fatigue_model

    def simulate_ascent(self):
        cumulative_fatigue = 0.0
        for i, hold in enumerate(self.route.holds):
            cost = self.fatigue_model.fatigue_cost(self.climber, hold)
            cumulative_fatigue += cost

            max_capacity = self.climber.strength * self.climber.endurance
            if cumulative_fatigue > max_capacity:
                print(f"Failed at hold {i+1} ({hold.grip_type}) with fatigue {cumulative_fatigue:.2f}")
                return False, cumulative_fatigue

            if i in self.route.rest_indices:
                cumulative_fatigue *= 0.8 

        print(f"Climb completed! Total fatigue: {cumulative_fatigue:.2f}")
        return True, cumulative_fatigue

    def monte_carlo(self, n_trials=100):
        results = []
        successes = 0
        for _ in range(n_trials):
            success, fatigue = self.simulate_ascent()
            results.append(fatigue)
            if success:
                successes += 1

        probability = successes / n_trials
        print(f"\nMonte Carlo Results ({n_trials} trials):")
        print(f"Average fatigue: {np.mean(results):.2f}")
        print(f"Minimum fatigue: {np.min(results):.2f}")
        print(f"Maximum fatigue: {np.max(results):.2f}")
        print(f"Success probability: {probability:.2%}")
        return probability
