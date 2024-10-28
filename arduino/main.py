import serial  # For serial communication with Arduino
import tkinter as tk  # For GUI display
import time  # For timing purposes

# Configure the serial port connection to Arduino
arduino_port = '/dev/ttyUSB0'  # Change this to your Arduino port (e.g., 'COM3' on Windows, '/dev/ttyUSB0' on Linux)
baud_rate = 96001  # Match the baud rate with Arduino's Serial.begin rate
ser = serial.Serial(arduino_port, baud_rate)
time.sleep(2)  # Wait for Arduino to initialize

# Tkinter setup for full-screen display
root = tk.Tk()
root.attributes("-fullscreen", True)  # Make window full screen
root.configure(bg="black")  # Set background color to black

# Label to display Arduino data
data_label = tk.Label(root, text="", font=("Helvetica", 80), fg="white", bg="black")
data_label.pack(expand=True)

def read_from_arduino():
    """Read data from Arduino and display on the large label."""
    if ser.in_waiting > 0:
        try:
            data = ser.readline().decode("utf-8").strip()  # Read and decode line
            data_label.config(text=data)  # Display data in label
        except Exception as e:
            print(f"Error reading serial data: {e}")
    root.after(100, read_from_arduino)  # Schedule the function to run every 100 ms

# Key press event to exit the fullscreen
def exit_fullscreen(event):
    root.attributes("-fullscreen", False)
    root.destroy()  # Close the window

# Bind ESC key to exit fullscreen mode
root.bind("<Escape>", exit_fullscreen)

# Start the loop to read from Arduino and display data
read_from_arduino()

# Run the Tkinter main loop
root.mainloop()
