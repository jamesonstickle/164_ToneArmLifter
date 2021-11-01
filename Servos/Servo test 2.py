import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)


pwm=GPIO.PWM(11, 25)
pwm.start(0)

pwm.ChangeDutyCycle(7.5) # neutral position
sleep(1)
pwm.ChangeDutyCycle(10) # right +90 deg position
sleep(1)

pwm.stop()


##def setAngle(angle):
##    duty = angle / 18 + 3
  ##  GPIO.output(11, True)
    ##pwm.ChangeDutyCycle(duty)
    ##sleep(1)
    ##GPIO.output(11, False)
    ##pwm.ChangeDutyCycle(duty)