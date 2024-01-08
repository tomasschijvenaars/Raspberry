#SOURCE is de powerpoints van vorig jaar
#GPIO voor functionaliteiten met pins
import RPi.GPIO as GPIO
#time om pauzes te defineren bij de leds
import time

#GPIO Pin waaraan led hangt defineren
Led = 23
GPIO.setmode(GPIO.BCM)
GPIO.setup(Led, GPIO.OUT)

#define functionaliteit
def opgC():
    while True:
        #Led gaat uit, wacht 0.1 seconden, gaat aan en wacht weer 0.1 seconden
        GPIO.output(Led, GPIO.LOW)
        time.sleep(0.1)
        GPIO.output(Led, GPIO.HIGH)
        time.sleep(0.1)
#functionaliteit uitvoeren
opgC()