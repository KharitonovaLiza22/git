import RPi.GPIO as GPIO

class PMW_DAC:
    def __init__(self, gpio_pin, pmw_frequency, dynamic_range, verbose = False):
        self.gpio_pin = gpio_pin
        self.pmw_frequency = pmw_frequency
        self.dynamic_range = dynamic_range
        self.verbose = verbose

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_pin, GPIO.OUT, initial = 0)
        self.pwm = GPIO.PWM(self.gpio_pin,self.pmw_frequency)
        self.pwm.start(0.0)

    def denit(self):
        self.pwm.stop
        GPIO.cleanup()

    def set_voltage(self, voltage):
        self.voltage = voltage
        if not (0.0 <= self.voltage <= self.dynamic_range):
            print(f"Напряжение выходит за динамический диапазон ЦАП (0.00 - {self.dynamic_range:.2f} B)")
            self.pwm.ChangeDutyCycle(0.0)
            return 0
        duty_cycle = (self.voltage / self.dynamic_range)*100
        print(f"Коэффицент заполнения: {duty_cycle:.2f}")
        self.pwm.ChangeDutyCycle(duty_cycle)

if __name__ == "__main__":
    try:
        dac = PMW_DAC(12, 500, 3.290, True)
        
        while True:
            try:
                voltage = float(input("Введите напряжение в Вольтах: "))
                dac.set_voltage(voltage)
            except ValueError:
                print("Вы не ввели число. Попробуйте ещё раз\n")

    except KeyboardInterrupt:
        print("\nПрограмма завершена пользователем")
    finally:
        dac.denit()