import os
import time

def rotate_screen(degrees):
    os.system(f'powershell.exe -Command "(Get-DisplayResolution).Rotate({degrees})"')

time.sleep(3)  # Gives you 3 seconds before it starts

while True:
    rotate_screen(90)   # Rotate right
    time.sleep(2)
    rotate_screen(180)  # Upside down
    time.sleep(2)
    rotate_screen(270)  # Rotate left
    time.sleep(2)
    rotate_screen(0)    # Back to normal
    time.sleep(2)
