import pandas as pd
import matplotlib.pyplot as plt

def visualize_rocket_flight():
    # Load data
    data = pd.read_csv('data/rocket_data.csv')

    # Create subplots
    fig, ax1 = plt.subplots()

    # Plot altitude
    ax1.set_xlabel('Time (s)')
    ax1.set_ylabel('Altitude (m)', color='blue')
    ax1.plot(data['Time (s)'], data['Altitude (m)'], color='blue', label='Altitude')
    ax1.tick_params(axis='y', labelcolor='blue')

    # Create a second y-axis for velocity
    ax2 = ax1.twinx()
    ax2.set_ylabel('Velocity (m/s)', color='red')
    ax2.plot(data['Time (s)'], data['Velocity (m/s)'], color='red', label='Velocity')
    ax2.tick_params(axis='y', labelcolor='red')

    # Add grid and title
    ax1.grid()
    plt.title('Rocket Simulation: Altitude and Velocity vs Time')
    fig.tight_layout()
    
    # Save the visualization
    plt.savefig('visuals/rocket_simulation.png')
    plt.show()

if __name__ == "__main__":
    visualize_rocket_flight()
