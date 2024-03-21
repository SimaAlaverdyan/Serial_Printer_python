import serial
import matplotlib.pyplot as plt
import time
from datetime import datetime

ser = serial.Serial('COM3', 115200)

time_data = []
angle_data = []

plt.ion()
fig, ax = plt.subplots()
line, = ax.plot(time_data, angle_data)

try:
    while True:
        # Read data from serial port
        data = ser.readline().decode().strip()
        if data:
            # x, y = map(float, data.split(','))
            # variables = data.split('\t')
            print("DATA BEFORE CONVERT " + data)
            x = datetime.now()
            y = float(data)
            print("\t\t\t", y)
            # print(y)
            time.sleep(1)
            time_data.append(x)
            angle_data.append(y)

            # Update plot
            line.set_xdata(time_data)
            line.set_ydata(angle_data)
            ax.relim()
            ax.autoscale_view()

            # Draw plot
            plt.xlabel('Time')
            plt.ylabel('Angle')
            plt.title('Real-time Angle Change')
            plt.grid(True)
            plt.draw()
            plt.pause(0.01)

except KeyboardInterrupt:
    ser.close()
    print("Serial port closed.")

# import serial
# import matplotlib.pyplot as plt
# import matplotlib.animation as animation
# from collections import deque
# from datetime import datetime

# # Initialize serial port
# ser = serial.Serial('COM3', 115200)

# # Initialize lists to store time and angle values
# time_values = deque(maxlen=100)  # Store last 100 time values
# angle_values = deque(maxlen=100)  # Store last 100 angle values

# # Function to update plot with new data
# def update_plot(frame):
#     # Read data from serial port
#     data = ser.readline().decode().strip()

#     # Split the data into individual variables using the comma as delimiter
#     variables = data.split(',')

#     # Check if we have received all 6 variables
#     if len(variables) == 6:
#         # Extract time and angle values
#         time_values.append(datetime.now())  # Append current time
#         angle_values.append(float(variables[2]))  # Append angle value
        
#         # Clear previous plot and plot new data
#         plt.cla()
#         plt.plot(time_values, angle_values)
#         plt.xlabel('Time')
#         plt.ylabel('Angle')
#         plt.title('Real-time Angle vs. Time')
#         plt.grid(True)

# ani = animation.FuncAnimation(plt.gcf(), update_plot, interval=100) 

# plt.show()