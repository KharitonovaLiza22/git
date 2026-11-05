import mcp3021_driver as mcp
import plot_weld as plt
import time
import RPi.GPIO as GPIO
import csv

duration=80.0
time_values=[]
voltage_values=[]
sampling_periods=[]
GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)

try:
    mcp3021=mcp.MCP3021(5.2)
    start_time=time.perf_counter()

    while (time.perf_counter() - start_time < duration):
        if ((time.perf_counter()-start_time) < (duration/2)):
            GPIO.output(14, 1)
        voltage_values.append(mcp3021.get_voltage())
        time_values.append(time.perf_counter()-start_time)
        if ((time.perf_counter()-start_time) > (duration/2)):
            GPIO.output(14, 0)
        time.sleep(0.0001)
    plt.plot_voltage_vs_time(time_values, voltage_values, max(voltage_values))
    with open("data.csv", "w", newline="") as file:
        writer=csv.writer(file, delimiter=" ")
        for voltage, times in zip(voltage_values, time_values):
            writer.writerow([voltage, times])
finally:
    GPIO.output(14, 0)
    mcp3021.deinit()