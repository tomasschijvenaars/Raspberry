#SOURCE ik heb de powerpoints van vorig jaar gebruikt
#ik heb ook mijn code van arduino aangehouden omdat dit dezelfde opzet is
# GPIO voor functionaliteiten met pins
import RPi.GPIO as GPIO
# time om pauzes te defineren bij de leds
import time

# GPIO Pin waaraan led hangt defineren
Led1 = 13
Led2 = 6
# GPIO Pin waaraan button hangt defineren
Btn1 = 25

GPIO.setmode(GPIO.BCM)
#We geven de led info, dus die setten we op output
GPIO.setup(Led1, GPIO.OUT)
GPIO.setup(Led2, GPIO.OUT)
#De knop willen we uitlezen, dus die zetten we op input.
GPIO.setup(Btn1, GPIO.IN, GPIO.PUD_DOWN)


# define functionaliteit
while True:
    #kleine sleep voor stabiliteit, voor mijn gevoel altans
    time.sleep(0.1)
    #input printen om te checken
    print(GPIO.input(Btn1))
    #als er niet op de knop wordt geklikt is hij LOW
    if GPIO.input(Btn1) == GPIO.LOW:
        GPIO.output(Led1, GPIO.LOW)

        GPIO.output(Led2, GPIO.HIGH)
    else:
        #functie volgens de opdracht uitvoeren
        print("button geklikt")
        GPIO.output(Led2, GPIO.LOW)

        GPIO.output(Led1, GPIO.HIGH)
        time.sleep(1.3)

        GPIO.output(Led2, GPIO.LOW)
        time.sleep(0.7)
