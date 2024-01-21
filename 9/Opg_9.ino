#include <IRremote.h>

//IR pin aangeven
const int irPin = 3;

//LED pins aangeven
const int ledPins[] = {10, 11, 12, 13};

//Default LED status is uit
int ledStatus[] = {LOW, LOW, LOW, LOW};

// Set up IR receiver and decode results
IRrecv irReceiver(irPin);
decode_results decodedResults;

void setup() {
  Serial.begin(9600);
  //De ledpins op output
  for (int i = 0; i < 4; i++) {
    pinMode(ledPins[i], OUTPUT);
  } 
  irReceiver.enableIRIn();
}

void loop() {
  //Millis houdt de tijd bij
  unsigned long currentTime = millis();

  if (irReceiver.decode(&decodedResults)) {
    Serial.println(decodedResults.value, HEX);
    irReceiver.resume();
    
    //Switch statement om de afstandbediening af te handelen
    switch (decodedResults.value) {
      case 0xFF30CF:
        digitalWrite(ledPins[0], HIGH);
        delay(50);
        digitalWrite(ledPins[0], LOW);
        Serial.println("selected 1");
        break;

      case 0xFF18E7:
        digitalWrite(ledPins[1], HIGH);
        delay(50);
        digitalWrite(ledPins[1], LOW);
        Serial.println("selected 2");
        break;
      
      case 0xFF7A85:
        digitalWrite(ledPins[2], HIGH);
        delay(50);
        digitalWrite(ledPins[2], LOW);
        Serial.println("selected 3");
        break;

      case 0xFF10EF:
        digitalWrite(ledPins[3], HIGH);
        delay(50);
        digitalWrite(ledPins[3], LOW);
        Serial.println("selected 4");
        break;
    }
  }
}
