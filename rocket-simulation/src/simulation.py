import numpy as np
import pandas as pd

# Constants
g = 9.81  # Gravity (m/s^2)
thrust = 15000  # Thrust force (N)
mass_initial = 5000  # Initial mass (kg)

def simulate_rocket_flight(duration=10, timestep=0.1):
    time_points = np.arange(0, duration, timestep)
    altitude = np.zeros_like(time_points)
    velocity = np.zeros_like(time_points)
    mass = mass_initial

    for i in range(1, len(time_points)):
        # Update mass (optional, if you want to simulate fuel consumption)
        mass -= 0.1  # Decrease mass due to fuel consumption
        
        # Calculate acceleration
        acceleration = thrust / mass - g
        
        # Update velocity and altitude
        velocity[i] = velocity[i - 1] + acceleration * timestep
        altitude[i] = altitude[i - 1] + velocity[i] * timestep

    # Save the data to CSV
    data = pd.DataFrame({'Time (s)': time_points, 'Altitude (m)': altitude, 'Velocity (m/s)': velocity})
    data.to_csv('data/rocket_data.csv', index=False)

if __name__ == "__main__":
    simulate_rocket_flight()
