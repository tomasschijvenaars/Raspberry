import RPi.GPIO as GPIO
import time

arduinoLED = 11
arduinoLED2 = 9
arduinoBTN = 13

check = 0

GPIO.setmode(GPIO.BCM)

#Ik heb de pins genoemd naar wat ze afvangen
#arduinoBTN krijgt een signaal van de arduino wanneer die detecteerd dat er op de knop wordt gedrukt
GPIO.setup(arduinoBTN, GPIO.IN)
#De led sturen signalen naar de arduino die dat doorgeven aan de ledlamp
GPIO.setup(arduinoLED, GPIO.OUT)
GPIO.setup(arduinoLED2, GPIO.OUT)

while True:
    time.sleep(0.1)
    #simpele bool switch
    if check == 0:
        GPIO.output(arduinoLED, GPIO.HIGH)
        GPIO.output(arduinoLED2, GPIO.LOW)
    else:
        GPIO.output(arduinoLED, GPIO.LOW)
        GPIO.output(arduinoLED2, GPIO.HIGH)

    if GPIO.input(arduinoBTN) == GPIO.HIGH:
        if check == 0:
            check = 1
        else:
            check = 0
        print("poep1")
