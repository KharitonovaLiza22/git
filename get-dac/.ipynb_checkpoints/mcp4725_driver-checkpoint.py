import smbus

class MCP4725:
    def __init__(self, dynamic_range, address=0x61, verbose = True):
        self.bus = smbus.SMBus ( 1 )
        self.dynamic_range = dynamic_range
        self.address = address
        self.verbose = verbose
        self.wm = 0x00
        self.pds = 0x00

    def denit(self):
        self.bus.close()

    def set_number(self,number):
        if not isinstance (number, int):
            print("На вход ЦАП можно подавать только целые числа")
            return
        if not (0<= number <= 4095):
            print("Число выходит за разрядность MCP4725 (12 бит)")
            return
        first_byte = self.wm | self.pds | (number >> 8)
        second_byte = number & 0xFF
        self.bus.write_byte_data(self.address, first_byte, second_byte)
        if self.verbose:
            i2c_address_byte = self.address << 1
            print(f"Число: {number}, отправленные по I2C данные: "
            f"[{hex(i2c_address_byte)},{hex(first_byte)},{hex(second_byte)}]")
    def set_voltage(self, voltage):
        min_v, max_v = self.dynamic_range
        if not (min_v <= voltage <= max_v):
            print (f"Напряжение выходит за динамический диапазон ЦАП({min_v:.2f} - {max_v:.2f} B)")
            return
        number = int (round((voltage / max_v)*4095))
        self.set_number(number)
if __name__ == "__main__":
    try:
        dac = MCP4725((0.0, 5.0), 0x61, True)
        
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