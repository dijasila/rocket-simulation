import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def animate_rocket_flight():
    # Load data
    data = pd.read_csv('data/rocket_data.csv')

    # Create a figure and axis
    fig, ax = plt.subplots()
    ax.set_xlim(0, data['Time (s)'].max())
    ax.set_ylim(0, data['Altitude (m)'].max() + 1000)  # Add some padding to the y-axis
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Altitude (m)')
    ax.set_title('Rocket Flight Animation')

    # Initialize a line that will be updated in the animation
    line, = ax.plot([], [], lw=2)

    # Function to initialize the animation
    def init():
        line.set_data([], [])
        return line,

    # Function to animate each frame
    def update(frame):
        line.set_data(data['Time (s)'][:frame], data['Altitude (m)'][:frame])
        return line,

    # Create animation
    ani = FuncAnimation(fig, update, frames=len(data), init_func=init, blit=True)

    # Save the animation
    ani.save('visuals/rocket_animation.gif', writer='imagemagick', fps=15)
    plt.show()

if __name__ == "__main__":
    animate_rocket_flight()
