# import matplotlib.pyplot as plt

# # Sample data
# x_data = [1, 2, 3, 4, 5]
# y_data = [10, 20, 25, 30, 35]

# # Create plot
# plt.plot(x_data, y_data)
# plt.xlabel('X-axis Label')
# plt.ylabel('Y-axis Label')
# plt.title('Sample Plot')
# plt.grid(True)
# plt.show()


import matplotlib.pyplot as plt
import matplotlib.animation as animation
from itertools import count

# Initialize figure and axis
fig, ax = plt.subplots()
x_vals = []
y_vals = []

# Function to update plot data
def animate(i):
    x_vals.append(next(index))
    y_vals.append(5)  # Replace your_data_function() with your function to get data from STM32F446RE
    ax.clear()
    ax.plot(x_vals, y_vals)
    ax.set_xlabel('X-axis Label')
    ax.set_ylabel('Y-axis Label')
    ax.set_title('Real-time Changing Plot')

# Create count iterator for x-axis
index = count()

# Create animation
ani = animation.FuncAnimation(fig, animate, interval=1000)  # Update plot every 1000 milliseconds (1 second)

# Show plot
plt.show()
