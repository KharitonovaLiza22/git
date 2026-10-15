import time
import RPi.GPIO as GPIO

class R2R_ADC:
    def __init__(self, dynamic_range, compare_time = 0.01, verbose = False):
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        self.compare_time = compare_time
        self.bits_gpio = [26, 20, 19, 16, 13, 12, 25, 11]
        self.comp_gpio = 21
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.bits_gpio, GPIO.OUT, initial = 0)
        GPIO.setup(self.comp_gpio, GPIO.IN)

    def number_to_dac(self, number):
        number = max(0, min(int(number), 255))
        bin_str = format(number, '08b')
        for i in range(8):
            GPIO.output(self.bits_gpio[i], int(bin_str[i]))

    def sequential_counting_adc(self):
        for num in range(256):
            self.number_to_dac(num)
            time.sleep(self.compare_time)
            if GPIO.input(self.comp_gpio) == 1:
                return num
        return 255

    def get_sc_voltage(self):
        digital_code = self.sequential_counting_adc()
        return (digital_code / 256.0) * self.dynamic_range

    def __del__(self):
        try:
            for pin in self.bits_gpio:
                GPIO.output(pin, 0)
            GPIO.cleanup()
        except Exception:
            pass

if __name__ == "__main__":
    DYNAMIC_RANGE_VOLTS = 3.3 
    adc = None
    try:
        adc = R2R_ADC(dynamic_range=DYNAMIC_RANGE_VOLTS)
        while True:
            voltage = adc.get_sc_voltage()
            print(f"Voltage: {voltage:.2f} V")
    finally:
        if adc is not None:
            adc.__del__()
