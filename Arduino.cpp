int PinoLed = 10;
void setup() {
  // put your setup code here, to run once:
  pinMode(PinoLed,OUTPUT);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(PinoLed,HIGH);
  Serial.println("Liga o LED");
  delay(1000);
  digitalWrite(PinoLed,LOW);
  Serial.println("Apaga o LED");
  delay(1000);
}


int PinoLedAm = 10;
int PinoLedVd = 11;
int PinoLedVm = 12;
void setup() {
  // put your setup code here, to run once:
  pinMode(PinoLedAm,OUTPUT);
  pinMode(PinoLedVd,OUTPUT);
  pinMode(PinoLedVm,OUTPUT);
  Serial.begin(9600);
}

////////////////////////////////////////////////////

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(PinoLedAm,HIGH);
  digitalWrite(PinoLedVd,LOW);
  digitalWrite(PinoLedVm,LOW);
  delay(3000);
  
  digitalWrite(PinoLedAm,LOW);
  digitalWrite(PinoLedVd,LOW);
  digitalWrite(PinoLedVm,HIGH);
  delay(3000);

  digitalWrite(PinoLedAm,LOW);
  digitalWrite(PinoLedVd,HIGH);
  digitalWrite(PinoLedVm,LOW);
  delay(3000);
}
