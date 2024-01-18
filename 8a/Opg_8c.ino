//GPIO van onderdelen die aan de arduino hangen
const int led1 = 4;
const int led2 = 5;
const int btn = 2;

int buttonState = 0; // var om btn te lezen
int berryState = 0;

int output = 0;

//GPIO die aan raspberry hangt
const int berryBtn = 13;
const int berryLed1 = 11;
const int berryLed2 = 10;
//Ik lees hier de button uit en stuur dan een signaal naar de Pi
//Deze stuurt dan een signaal terug wat de arduino doorgeeft aan de lampjes
void setup() {
  pinMode(led1, OUTPUT);  //
  pinMode(led2, OUTPUT);  // 
  pinMode(btn, INPUT); // 
//deze staan tegenovergesteld van wat ze normaal staan omdat ze hun signaal sturen en ontvangen van de Pi
  pinMode(berryBtn, OUTPUT); //geeft status van de button door
  pinMode(berryLed1, INPUT); //vangt status voor lichtjes
  pinMode(berryLed2, INPUT); //vangt status voor lichtjes
}

void loop() {
  digitalWrite(led1, digitalRead(berryLed1));
  digitalWrite(led2, digitalRead(berryLed2));
  digitalWrite(berryBtn, digitalRead(btn));
}
