#include <ArduinoJson.h>
#include "EspMQTTClient.h"

//Configuração do MQTT
EspMQTTClient client{
  "xxxxxxxxx",  //SSID do WiFi
  "xxxxxxxxx",      //Senha do WiFi
  "mqtt.tago.io",   //Endereço do servidor
  "Default",        //Usuário
  "xxxxxxxxxxxxx",  //Token do device
  "esp" ,           //Nome do device
  1883              //Porta de comunicação
};

void setup() {
  Serial.begin(9600);
  Serial.println("Conectando o WiFi");
  while(!client.isWifiConnected()){
    Serial.print('.'); client.loop(); delay(1000);
  }
  Serial.println("WiFi Conectado");

  Serial.println("Conectando com o Servidor MQTT");
  while(!client.isMqttConnected()){
    Serial.print('.'); client.loop(); delay(1000);
  }
  Serial.println("MQTT Conectado");
}

//Callback da EspMQTTClient
void onConnectionEstablished(){
  }

  char bufferJson[100];
  int temperatura = 0;
  
void loop() {
  temperatura = random(0,100);

  StaticJsonDocument<300> documentoJson;
  documentoJson["variable"] = "temperatura";
  documentoJson["value"] = temperatura;
  documentoJson["unit"] = "celsius";

  serializeJson(documentoJson, bufferJson);
  Serial.println(bufferJson);
  client.publish("topicoTDSPI", bufferJson);
  delay(5000);
  client.loop();
}
