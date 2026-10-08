import r2r_dac as r2r
import signal_generator as sg
import time
import RPi.GPIO as GPIO

amplitude = 3.183
signal_frequency = 10
sampling_frequency = 1000

dac = None

try:
    dac = r2r.R2R_DAC([16, 20, 21, 25, 26, 17, 27, 22], 3.183, False)
    start_time = time.time()
    
    while True:
        current_time = time.time() - start_time
        norm_amp = sg.get_triangle_wave_amplitude(signal_frequency, current_time)
        target_voltage = norm_amp * amplitude
        
        number = dac.set_voltage(target_voltage)
        dac_bits = dac.set_number(number)
        GPIO.output(dac.gpio_bits, dac_bits)
        
        sg.wait_for_sampling_period(sampling_frequency)

except KeyboardInterrupt:
    pass

finally:
    if dac is not None:
        dac.denit()
