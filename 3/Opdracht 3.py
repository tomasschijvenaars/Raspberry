#SOURCE is de powerpoints van vorig jaar
#GPIO voor functionaliteiten met pins
import RPi.GPIO as GPIO
#time om pauzes te defineren bij de leds
import time

#GPIO Pin waaraan led hangt defineren
Led1 = 23
Led2 = 24
#We geven de led info, dus die setten we op output
GPIO.setmode(GPIO.BCM)
GPIO.setup(Led1, GPIO.OUT)
GPIO.setup(Led2, GPIO.OUT)

#define functionaliteit
while True:
    #Led 1 gaat aan, wacht 1.3 seconden, gaat uit, wacht 0.7 seconden
    GPIO.output(Led1, GPIO.HIGH)
    time.sleep(1.3)
    GPIO.output(Led1, GPIO.LOW)
    time.sleep(0.7)
    #Led 2 gaat aan, wacht 0.8 seconden, gaat uit, wacht 1.7 seconden
    GPIO.output(Led2, GPIO.HIGH)
    time.sleep(0.8)
    GPIO.output(Led2, GPIO.LOW)
    time.sleep(1.7)

