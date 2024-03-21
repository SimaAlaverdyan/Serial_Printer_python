import serial

ser = serial.Serial('COM3', 115200)

try:
    while True:
        data = ser.readline().decode().strip()
        
        variables = data.split('\t')            # -------- variable[2] is angle from MPU6050

        print(data)
        

except KeyboardInterrupt:
    ser.close()
    print("Serial port closed.")