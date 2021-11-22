import RPi.GPIO as GPIO
import time


GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    input_state = GPIO.input(19)
    if input_state == False:
        print('Button Pressed')
        time.sleep(0.2)
