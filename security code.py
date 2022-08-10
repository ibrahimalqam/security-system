from ultrasonic import Ultrasonic
from microbit import *
from ssd1306 import initialize, clear_oled
from ssd1306_text import add_text

initialize()
clear_oled()
sleep(1000)

ultrasonic_sensor = Ultrasonic()

while True:
    distance_value = ultrasonic_sensor.measure_distance_cm()
    motion = pin1.read_digital()
    
    if motion:
        if distance_value < 10 :
            add_text(0, 0, "danger")
            add_text(0, 1, "is close")
            pin0.write_digital(1)
        else :
            pin0.write_digital(0)
            clear_oled()
