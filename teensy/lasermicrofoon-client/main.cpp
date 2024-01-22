#include <Arduino.h>
#include "Wire.h"
#include "Audio.h"

#define I2C_ESP_ADRS 0x1


AudioSynthWaveform       wav1;
AudioRecordQueue         queue;     //xy=504,468
AudioConnection          patchCord1(wav1, queue);
AudioO
void setup() {
  Serial.begin(115200);

  while (!Serial) ; 
  AudioMemory(20);

  if (CrashReport){
    CrashReport.printTo(Serial);
    CrashReport.clear();
  }
  delay(1e3);

  Wire1.begin();

  wav1.begin(0.5,220.0,WAVEFORM_SINE);
  queue.begin();

  // put your setup code here, to run once:
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
 
  // Serial.println(queue.available());

  // while (queue.available() > 0)
  // {
  //   byte buffer[512];
    
  //   memcpy(buffer, queue.readBuffer(), 256);
  //   queue.freeBuffer();
  //   memcpy(buffer+256, queue.readBuffer(), 256);
  //   queue.freeBuffer();

  //   // Serial.println(sizeof(buffer));
  //   // Wire1.beginTransmission(I2C_ESP_ADRS);
  //   // Wire1.write(buffer, 1);
  //   // Wire1.endTransmission(true);
  // }
  // byte test[1] = {0x10};
  

  // char test[512];
  // for (int i = 0; i < 511; i++){
  //   test[i] = (char )i;
  // }
  // Serial.println((String)test);

  // Wire1.beginTransmission(I2C_ESP_ADRS);
  // digitalWrite(LED_BUILTIN, HIGH);
  // // Wire1.write(test);
  // Wire1.write("");
  // Wire1.endTransmission(true);
  // digitalWrite(LED_BUILTIN, LOW);
  // delay(1000);
  // put your main code here, to run repeatedly:
}
 