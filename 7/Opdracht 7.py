#SOURCE is powerpoint op brightspace
import RPi.GPIO as GPIO
#deze lib is nodig om de moter te gebruiken
from RpiMotorLib import RpiMotorLib

GPIO.setmode(GPIO.BCM)

#De setup van de buttons
btn1 = 13
btn2 = 26
GPIO.setup(btn1, GPIO.IN, GPIO.PUD_UP)
GPIO.setup(btn2, GPIO.IN, GPIO.PUD_UP)


#De GPIO pins waaraan de motor hangt
motorPins = [11, 9, 22, 27]
motor = RpiMotorLib.BYJMotor("MOTOR", "28BYJ")

while True:
    #Naar links draaien
    if (GPIO.input(btn1) == GPIO.HIGH):
        #Een compleet rondje is 512 stappen
        #Als je 5 seconden deelt door 512 krijgen je ongeveer 0.01
        #De counter clockwise parameter moet op true om naar links te gaan
        print("button 1")
        motor.motor_run(motorPins, .001, 100, True, False, "half", 0)

    #Naar rechts draaien
    if (GPIO.input(btn2) == GPIO.HIGH):
        #Hetzelfde als hierboven
        #12 seconden delen door 512 stappen is ongeveer  0.0234 en parameter counter clockwise op false om naar rechts te gaan
        print("button 2")
        motor.motor_run(motorPins, .00234, 100, False, False, "half", 0)
