#include <Audio.h>
#include <Wire.h>
#include <SPI.h>
#include <SD.h>
#include <SerialFlash.h>

// GUItool: begin automatically generated code
AudioSynthWaveformSine   sine1;          //xy=121,99
AudioOutputI2S2          i2s2_1;         //xy=434,71
AudioConnection          patchCord1(sine1, i2s2_1);
// GUItool: end automatically generated code


void setup() {                
  Serial.begin(115200);
  AudioMemory(20);

  while (!Serial); 

  if (CrashReport){
    CrashReport.printTo(Serial);
    CrashReport.clear();
  }

  sine1.frequency(220);
  // que.begin();

}

void loop() {
  Serial.println(sine1.processorUsage());
  Serial.println(i2s2_1.processorUsage());
  delay(300);
  // wave.update();
  // is22.update();

}