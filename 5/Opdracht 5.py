# GPIO voor functionaliteiten met pins
import RPi.GPIO as GPIO
# time om pauzes te defineren bij de leds
import time

# GPIO Pin waaraan led hangt defineren
Led1 = 13
Led2 = 6
# GPIO Pin waaraan button hangt defineren
Btn1 = 25

prevTime = 0

bufferTime = 1300

GPIO.setmode(GPIO.BCM)
GPIO.setup(Led1, GPIO.OUT)
GPIO.setup(Led2, GPIO.OUT)
GPIO.setup(Btn1, GPIO.IN)
check = 0

#millis om de delays te fixen
def millis():
    return time.time()*1000

while True:
    time.sleep(0.1)
    #de tijd op nu setten voor de check
    timeNow = millis()
    print(GPIO.input(Btn1))
    print(check)
    if GPIO.input(Btn1) == GPIO.LOW:
        #simpele bool switch om per klik iets anders te krijgen
        if check == 0:
            check = 1
            #andere led uit
            GPIO.output(Led2, GPIO.LOW)
            if (timeNow - 1000 >= prevTime):
                # GPIO.HIGH is hetzelfde als 1
                if (Led1 == 1):
                    GPIO.output(Led1, GPIO.LOW)
                else:
                    GPIO.output(Led1, GPIO.HIGH)
        else:
            check = 0
            #Led 1 uit
            GPIO.output(Led1, GPIO.LOW)
            #deze is hetzelde als bij de if alleen pas je ook de knippertijd aan in de buffertijd variabele
            if (timeNow - bufferTime >= prevTime):
                if (Led2 == 1):
                    GPIO.output(Led2, GPIO.LOW)
                    bufferTime = 700
                else:
                    GPIO.output(Led2, GPIO.HIGH)
                    bufferTime = 1300
