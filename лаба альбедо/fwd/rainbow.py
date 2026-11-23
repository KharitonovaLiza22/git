import subprocess
import sys

shutter = sys.argv[1]          # выдержка из п2.1, мкс
sheets = ["white", "red", "yellow", "green", "blue", "white-repeat"]

for sheet in sheets:
    input("Положите лист «%s» на то же место и нажмите Enter..." % sheet)
    name = sheet.replace("white-repeat", "white-tungsten-repeat") if sheet == "white-repeat" else sheet + "-tungsten"
    subprocess.run(["python3", "lightMeasure.py", name, shutter], check=True)