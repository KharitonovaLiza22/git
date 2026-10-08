import mcp4725_driver as mcp
import signal_generator as sg
import time

amplitude = 3.3
signal_frequency = 10
sampling_frequency = 200

dac = None

try:
    dac = mcp.MCP4725((0.0, 3.3), 0x61, False)
    start_time = time.time()
    
    while True:
        current_time = time.time() - start_time
        norm_amp = sg.get_sin_wave_amplitude(signal_frequency, current_time)
        target_voltage = norm_amp * amplitude
        
        dac.set_voltage(target_voltage)
        
        sg.wait_for_sampling_period(sampling_frequency)

except KeyboardInterrupt:
    pass

finally:
    if dac is not None:
        dac.denit()
