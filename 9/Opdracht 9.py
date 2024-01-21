import RPi.GPIO as GPIO
import time

#GPIO pins die aan de leds en arduino hangen
ledGPIOs = [3, 4, 17, 27]
arduinoGPIOs = [26, 19, 13, 6]

#knippersnelheiden voor de leds
blinkingSpeeds = [250, 500, 750, 1000]
#de snelheid waar de lampen mee beginnen
setSpeed = [250, 500, 750, 1000]

#Er moeten altijd 2 leds aan staan
minActiveLEDs = 2
previousTimes = [0, 0, 0, 0]

#Variabele om de geselecteerde knop bij te houden
selectedButton = -1
selectedLed = -1

GPIO.setmode(GPIO.BCM)

#GPIO setup voor input en output
for pin in ledGPIOs:
    GPIO.setup(pin, GPIO.OUT)

for pin in arduinoGPIOs:
    GPIO.setup(pin, GPIO.IN)

#Millis om de tijd bij te houden
def millis():
    return time.time() * 1000

#Delay zetten voor een led
def changeDelay(led, selectedButton):
    blinkingSpeeds[led] = activeSpeed[selectedButton]

#Functie om de geselecteerde knop die de arduino terugstuurd af te handelen
def checkForInput():
    global selectedButton
    global selectedLed
    i = 0
    while i < 4:
        if GPIO.input(arduinoGPIOs[i]):
            time.sleep(0.1)
            selectedButton = i
            if selectedLed == -1:
                selectedLed = i
                print(selectedLed)
            else:
                setDelay(selectedLed, blinkingSpeeds[selectedButton])
                selectedLed = -1
        i += 1

while True:
    checkForInput()
    global prevTimes
    i = 0
    while i < 4:
        # Hier wordt bijgehouden of er genoeg tijd is voorbijgegaan om te knipperen
        # Het lampje gaat dan aan of uit als de tijd voorbij is
        if millis() - prevTimes[i] >= delays[i]:
            prevTimes[i] = millis()
            if GPIO.input(ledPins[i]):
                GPIO.output(ledPins[i], GPIO.LOW)
            else:
                GPIO.output(ledPins[i], GPIO.HIGH)
        i += 1
