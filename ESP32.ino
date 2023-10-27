#include "Arduino.h"
#include "WiFi.h"
#include "HTTPClient.h"
#include "DHT.h"

HTTPClient client;
DHT dht(4, DHT11);

char wifiSsid[] = "xxxxxxx";
char wifiPass[] = "xxxxxxx";

char server[] = "https://api.tago.io/data";
char header[] = "application/json";
char token[] = "40d76eba-4906-4789-87f6-e9bc19cd28fc";

void initWifi(){
  Serial.println("Conectando no WiFi");
  WiFi.begin(wifiSsid, wifiPass);
  while(WiFi.status() != WL_CONNECTED){
    Serial.println(".");
    delay(1000);
  }
  Serial.println("Conectado");
  Serial.println(WiFi.localIP());
}

void setup() {
  Serial.begin(9600);
  initWifi();
  dht.begin();
}

float temperatura = 0;
float umidade = 0;

void loop() {
  char anyData[30];
  char postData[300];
  char anyData1[30];
  char bAny[30];
  int status = 0;

  strcpy(postData, "{\n\t\"variable\": \"Temperatura\", \n\t\"value\" : ");
  dtostrf(temperatura, 6, 2, anyData);
  strncat(postData, anyData, 100);
  strcpy(anyData1, ", \n\t\"unit\": \"C\"\n\t}\n");
  strncat(postData, anyData1, 100);

  client.begin(server);
  client.addHeader("Content-Type", header);
  client.addHeader("Device-Token", token);
  client.POST(postData);

  Serial.println(postData);
  Serial.println(status);
  temperatura = dht.readTemperature();
  umidade = dht.readHumidity();

  strcpy(postData, "{\n\t\"variable\": \"Umidade\", \n\t\"value\" : ");
  dtostrf(umidade, 6, 2, anyData);
  strncat(postData, anyData, 100);
  strcpy(anyData1, ", \n\t\"unit\": \"%\"\n\t}\n");
  strncat(postData, anyData1, 100);

  client.begin(server);
  client.addHeader("Content-Type", header);
  client.addHeader("Device-Token", token);
  client.POST(postData);
  
  delay(5000);
}
