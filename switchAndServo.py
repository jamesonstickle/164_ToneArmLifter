import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)      # Define the Pin numbering type. Here we are using BCM type

# 18 is the button
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# 19 is the servo
servo_pin = 19 # GPIO Pin where servo is connected

# Defining Servo Pin as output pin
GPIO.setup(servo_pin, GPIO.OUT)

pwm = GPIO.PWM(servo_pin, 50)  # PWM channel at 50 Hz frequency

pwm.start(0) # Zero duty cycle initially

button = True

while True:
    input_state = GPIO.input(18)
    if input_state == False:
        print('Button Pressed')
        if button == True:
            print('Button is True')
            time.sleep(1)
            pwm.ChangeDutyCycle(4)
            button = False
        else:
            print ('Button is False')
            time.sleep(1)
            #Pause the servo
            pwm.ChangeDutyCycle(11)
            button = True
        

