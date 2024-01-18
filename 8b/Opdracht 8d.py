import RPi.GPIO as GPIO
import time

#GPIO die aan arduino hangt
arduinoLED = 11
arduinoLED2 = 9
arduinoBTN = 13
#de knopjes en leds
btn = 22
led1 = 17
led2 = 4

GPIO.setmode(GPIO.BCM)
#de normale setup voor knoppen en leds, de signalen geven we door aan de arduino
GPIO.setup(btn, GPIO.IN)
GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)
#de data die we terugkrijgen van de arduino
GPIO.setup(arduinoBTN, GPIO.OUT)
GPIO.setup(arduinoLED, GPIO.IN)
GPIO.setup(arduinoLED2, GPIO.IN)

#alles wat in deze loop gebeurd is het koppelen van de input en de output
while True:
    time.sleep(0.1)
    #de output van de fysieke knop sturen we door naar de arduino
    GPIO.output(arduinoBTN, GPIO.input(btn))
    #de output van de fysieke leds krijgen we terug van de arduino
    GPIO.output(led1, GPIO.input(arduinoLED))
    GPIO.output(led2, GPIO.input(arduinoLED2))

    print(GPIO.input(arduinoLED))
