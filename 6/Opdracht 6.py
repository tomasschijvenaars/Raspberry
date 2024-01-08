#SOURCE powerpoint vorig jaar 2: buttons en servo
#ook hulp gekregen van oud klasgenoten
# GPIO voor functionaliteiten met pins
import RPi.GPIO as GPIO
# time om pauzes te defineren bij de leds
import time

# GPIO Pin waaraan servo hangt defineren
Servo = 6
# GPIO Pin waaraan button hangt defineren
Btn1 = 25
Btn2 = 9

GPIO.setmode(GPIO.BCM)
#naar de servo sturen we data, dus op output
GPIO.setup(Servo, GPIO.OUT)
servo_pwm = GPIO.PWM(Servo, 50)
servo_pwm.start(0)

# Knop instellen zodat PUD_DOWN de trigger is voor detectie
GPIO.setup(Btn1, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(Btn2, GPIO.IN, GPIO.PUD_DOWN)


def millis():
    return time.time() * 1000

# turnServo wil weten naar welke graden hij moet draaien en hoelang hij moet wachten tot hij terug moet
def turnServo(degree, pause):
    #deze formule houdt ik aan omdat deze zo in de powerpoint staat
    temp = degree / 18 + 2
    servo_pwm.ChangeDutyCycle(temp)
    time.sleep(pause)
    servo_pwm.ChangeDutyCycle(temp)

while True:
    # Wanneer er input van button 1 wordt gedetecteerd gaat de servo naar 120 graden en wacht hij 1 seconden voordat hij teruggaat naar 0.
    if GPIO.input(Btn1) == GPIO.HIGH:
        print("test1")
        turnServo(120, 1)
        turnServo(0, 1)

    # Wanneer er input van button 2 wordt gedetecteerd gaat de servo naa 120 graden en wacht hij 0.5 seconden voordat hij teruggaat naar 0.
    if GPIO.input(Btn2) == GPIO.HIGH:
        print("test2")
        turnServo(120, 0.5)
        turnServo(0, 0.5)
