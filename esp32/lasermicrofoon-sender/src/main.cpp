#include <Arduino.h>
#include "Wire.h"

#define I2C_ESP_ADRS 0x1
int i = 0; 

void onReceive(int len){ 
  Serial.printf("onReceive[%d]: ", len);
  digitalWrite(LED_BUILTIN, HIGH);
  byte buffer[512]; 

  while (Wire.available()){
    Wire.readBytes(buffer, sizeof(byte)*512*2);
  }

  Serial.println(sizeof(buffer));
  digitalWrite(LED_BUILTIN, LOW);

}

void onRequest(){
  Wire.print(i++);
  Wire.print(" Packets.");
  Serial.println("onRequest");
}


void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  Wire.onReceive(onReceive);
  Wire.onRequest(onRequest);
  Wire.setBufferSize(25e3);
  Wire.begin(I2C_ESP_ADRS);

  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:

}
