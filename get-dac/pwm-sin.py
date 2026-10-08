import pwm_dac as pwm
import signal_generator as sg
import time

amplitude = 3.290
signal_frequency = 10
sampling_frequency = 1000

dac = None

try:
    dac = pwm.PMW_DAC(12, 500, 3.290, True)
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
