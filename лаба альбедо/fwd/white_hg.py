import os
import subprocess
import sys

import imageio.v2 as imageio

if len(sys.argv) != 3:
    print("Использование: python3 lightMeasure.py <имя> <выдержка, мкс>")
    sys.exit(1)

name = sys.argv[1]          # имя снимка без .png
shutter = sys.argv[2]       # выдержка, мкс
print(shutter)

os.makedirs("data", exist_ok=True)
fileName = "data/" + name + ".png"

# 1. Съёмка: постоянные разрешение, усиление и баланс белого
subprocess.run(["raspistill", "-n", "-t", "1000", "-w", "2560", "-h", "1440", "-rot", "180",
                "-ss", shutter, "-ISO", "100", "-awb", "off", "-awbg", "1.5,1.5",
                "-e", "png", "-o", fileName], check=True)

# 2. Проверка: максимум по каналам R, G, B
photo = imageio.imread(fileName)[:, :, :3]   # четвёртый канал служебный
top = photo.max(axis=(0, 1))
print("%s: R=%d G=%d B=%d" % (name, top[0], top[1], top[2]))

# 3. Предупреждения
if top.max() == 255:
    print("ПЕРЕСВЕТ: где-то 255, выдержку надо уменьшить (например, вдвое).")
elif top.max() < 150:
    print("Снимок тёмный: максимум меньше 150, выдержку можно увеличить.")
else:
    print("Выдержка в норме.")