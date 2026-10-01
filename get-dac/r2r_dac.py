import RPi.GPIO as GPIO

class R2R_DAC:
    def __init__(self, gpio_bits, dynamic_range, verbose = False):
        self.gpio_bits = gpio_bits
        self.dynamic_range = dynamic_range
        self.verbose = verbose

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_bits, GPIO.OUT, initial = 0)

    def denit(self):
                    GPIO.output(self.gpio_bits, 0)
                    GPIO.cleanup()

    def set_number(self,number):
        self.number = number
        return [int(e) for e in bin(number)[2:].zfill(8)]

    def set_voltage(self, voltage):
        self.voltage = voltage
        if not (0.0 <= self.voltage <= self.dynamic_range):
            print(f"Напряжение выходит за динамический диапазон ЦАП (0.00 - {self.dynamic_range:.2f} B)")
            print("Устанавливаем 0.0 В")
            return 0
        return int(self.voltage / self.dynamic_range * 255)

if __name__ == "__main__":
    try:
        dac = R2R_DAC([16, 20, 21, 25, 26, 17, 27, 22], 3.183, True)
        
        while True:
            try:
                voltage = float(input("Введите напряжение в Вольтах: "))
                number = dac.set_voltage(voltage)
                dac_bits = dac.set_number(number)
                GPIO.output(dac.gpio_bits, dac_bits)
            except ValueError:
                print("Вы не ввели число. Попробуйте ещё раз\n")

    except KeyboardInterrupt:
        print("\nПрограмма завершена пользователем")
    finally:
        dac.denit()