from flask import Flask, render_template_string, request   # Importing the Flask modules 
import RPi.GPIO as GPIO     # Importing the GPIO library 

from time import sleep      # Import sleep module from time library

servo_pin = 19 # GPIO Pin where servo is connected

GPIO.setmode(GPIO.BCM)      # Define the Pin numbering type. Here we are using BCM type

# Defining Servo Pin as output pin
GPIO.setup(servo_pin, GPIO.OUT)

pwm = GPIO.PWM(servo_pin, 50)  # PWM channel at 50 Hz frequency

pwm.start(0) # Zero duty cycle initially
app = Flask(__name__)
#HTML Code 
TPL = '''
<html>
     <img src="https://pbs.twimg.com/profile_images/3052476436/cd91b441502ae051e880465fbac39045_400x400.jpeg" alt="">
    <head><title>Web Page to Control Servo</title></head>
    <body>
    <h2> DAVE LOOK IT WORKS!!!!</h2>
        <form method="POST" action="test">
            <h3> make it go</h3>
            <p>Slider   <input type="range" min="1" max="12.5" name="slider" /> </p>
            <input type="submit" value="submit" />
        </form>
    </body>
</html>

'''
@app.route("/")
def home():                                                                                                                                                         
    return render_template_string(TPL)                        
@app.route("/test", methods=["POST"])
def test():
    # Get slider Values
    slider = request.form["slider"]
    # Change duty cycle
    pwm.ChangeDutyCycle(float(slider))
    print('Here is slider value: ', slider)
    sleep(0.5)
    # Pause the servo
    pwm.ChangeDutyCycle(0)
    return render_template_string(TPL)

# Run the app on the local development server
if __name__ == "__main__":
    app.run()