//led pin en buttonpin aanspreken
const int ledPin1 = 10;   
const int ledPin2 = 11;        
const int buttonPin = 13;

int buttonState = 0;          //variabele om button te lezen
int check = 0;
unsigned long prevTime = 0;

void setup() {
  pinMode(ledPin1, OUTPUT);    //Ledpin aanspreken
  pinMode(ledPin2, OUTPUT);    //Ledpin aanspreken
  pinMode(buttonPin, INPUT);  //Buttonpin aanspreken
  
  Serial.begin(9600);
}

void loop() {
  //kleine delay voor gevoeligheid
  delay(100);
  Serial.println(digitalRead(buttonPin));
   unsigned long curTime = millis();
  //uitlezen status die de Pi meegeeft
  if (digitalRead(buttonPin) == HIGH){
    //zorgen dat hij dit maar 1 keer per seconden kan switchen voor stabiliteit
    if (curTime - prevTime >= 1000){
      prevTime = curTime;
      if(check == 0){
        //leds aan en uit wisselen
        digitalWrite(ledPin1, HIGH);
        digitalWrite(ledPin2, LOW);
        check = 1;
        Serial.println("1 aan");
      } else {
        digitalWrite(ledPin1, LOW);
        digitalWrite(ledPin2, HIGH);
        check = 0;
        Serial.println("2 aan");
      }
    }
  }
}
