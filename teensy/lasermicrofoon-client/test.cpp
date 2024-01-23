#include <Arduino.h>
#include <SPI.h>
#include "Audio.h"

// MASTERRR

#define MOSI_PIN 11
#define MISO_PIN 12
#define CS_PIN 10
#define SCLK_PIN 13

#define SPI_CLOCK_SPEED 4000000
#define NBLOX 4

AudioSynthWaveformSine wave;
AudioRecordQueue que;
AudioConnection cable(wave, 0, que, 0);
AudioConnection cable2(wave, 0, que, 1);

// SPISettings spi_settings()

void setup()
{
  
  AudioMemory(16);
  
  Serial.begin(115200);
  
  while (!Serial)
    ;

  if (CrashReport)
  {
    CrashReport.printTo(Serial);
    CrashReport.clear();
  }

  SPI.begin();

  wave.frequency(300.f);
  que.begin();
}

void loop()
{
  // SPI.beginTransaction(())
  // SPI.transfer16()
  
  // Serial.println(que.available());
  // delay(200);

  if (que.available() > 2)
  {
    // Serial.println("more than 2");
    SPI.beginTransaction(SPISettings(SPI_CLOCK_SPEED, MSBFIRST, SPI_MODE3));
    // digitalWrite(SS, LOW);
    while (que.available() > 2)
    {
      //  Serial.println("more than 2 while");
      // for (int i = 0; i < 2; i++)
      // {
        
      byte buffer[AUDIO_BLOCK_SAMPLES * sizeof(uint16_t)];
      memcpy(buffer, que.readBuffer(), AUDIO_BLOCK_SAMPLES*sizeof(uint16_t));
      // SPI.transfer(buffer, sizeof(buffer));
      SPI.transfer16((uint16_t)1);
      que.freeBuffer();
      // }     
    }
    SPI.endTransaction();
  }
}

// #include <Arduino.h>
// // #include <SPI.h>
// #include <stdio.h>
// #include <stdint.h>
// #include <stddef.h>
// #include <string.h>

// #include "freertos/FreeRTOS.h"
// #include "freertos/task.h"
// #include "freertos/semphr.h"
// #include "freertos/queue.h"

// #include "lwip/sockets.h"
// #include "lwip/dns.h"
// #include "lwip/netdb.h"
// #include "lwip/igmp.h"

// #include "esp_wifi.h"
// #include "esp_system.h"
// #include "esp_event.h"
// #include "nvs_flash.h"
// #include "soc/rtc_periph.h"
// #include "driver/spi_slave.h"
// #include "esp_log.h"
// #include "esp_spi_flash.h"
// #include "driver/gpio.h"
// // SLAVEE

// #define MOSI_PIN GPIO_NUM_13
// #define MISO_PIN GPIO_NUM_12
// #define CS_PIN GPIO_NUM_15
// #define SCLK_PIN GPIO_NUM_14

// #define SPI_CLOCK_SPEED 1000000

// // Configuration for the SPI bus
// spi_bus_config_t buscfg = {
//     .mosi_io_num = MOSI_PIN,
//     .miso_io_num = MISO_PIN,
//     .sclk_io_num = SCLK_PIN,
//     .quadwp_io_num = -1,
//     .quadhd_io_num = -1,
// };

// // Configuration for the SPI slave interface
// spi_slave_interface_config_t slvcfg = {
//     .spics_io_num = CS_PIN,
//     .flags = 0,
//     .queue_size =3,
//     .mode = 3};

//  spi_slave_transaction_t t, *ptr2;
//   byte recvbuf[128*sizeof(uint16_t)], *ptr; 

//  esp_err_t ret;
// void setup()
// {
//   // SPI.begin(SCLK_PIN, MISO_PIN, MOSI_PIN, CS_PIN);
//   Serial.begin(115200);

//   gpio_set_pull_mode(MOSI_PIN, GPIO_PULLUP_ONLY);
//     gpio_set_pull_mode(SCLK_PIN, GPIO_PULLUP_ONLY);
//     gpio_set_pull_mode(CS_PIN, GPIO_PULLUP_ONLY);

//   ret = spi_slave_initialize(HSPI_HOST, &buscfg, &slvcfg, SPI_DMA_CH_AUTO);
//   assert(ret==ESP_OK);
//   memset(recvbuf, 0, 33);
//   memset(&t, 0, sizeof(t));
  
// }

// void loop()
// {
//   Serial.println(digitalRead(CS_PIN));
//   memset(recvbuf, 0, 128*2U);
//   t.length=128*8;
//   t.rx_buffer=recvbuf;
//   spi_slave_queue_trans(HSPI_HOST, &t, portMAX_DELAY);
  
//   spi_slave_get_trans_result(HSPI_HOST, &ptr2, portMAX_DELAY);
//   // ret = spi_slave_transmit(HSPI_HOST, &t, portMAX_DELAY);
//   Serial.printf("Received: %s\n", recvbuf);
// }

// ESP32DMASPI::Slave slave;

// static const uint32_t BUFFER_SIZE = 128*16;
// uint8_t* spi_slave_tx_buf;
// uint8_t* spi_slave_rx_buf;

// void set_buffer() {
//     for (uint32_t i = 0; i < BUFFER_SIZE; i++) {
//         spi_slave_tx_buf[i] = (0xFF - i) & 0xFF;
//     }
//     memset(spi_slave_rx_buf, 0, BUFFER_SIZE);
// }

// void setup() {
//     Serial.begin(115200);

//     // to use DMA buffer, use these methods to allocate buffer
//     spi_slave_tx_buf = slave.allocDMABuffer(BUFFER_SIZE);
//     spi_slave_rx_buf = slave.allocDMABuffer(BUFFER_SIZE);

//     set_buffer();
//     delay(5000);

//     Serial.println("test");

//     // slave device configuration
//     slave.setDataMode(SPI_MODE0);
//     slave.setMaxTransferSize(BUFFER_SIZE);
//     slave.setQueueSize(3);

//     // begin() after setting
//     // note: the default pins are different depending on the board
//     // please refer to README Section "SPI Buses and SPI Pins" for more details
//     slave.begin(HSPI, SCLK_PIN, MISO_PIN, MOSI_PIN, CS_PIN);  // HSPI
// }

// void loop() {
//     // if there is no transaction in queue, add transaction
//     if (slave.remained() == 0) {
//         slave.queue(spi_slave_rx_buf, spi_slave_tx_buf, BUFFER_SIZE);
//     }

//     // if transaction has completed from master,
//     // available() returns size of results of transaction,
//     // and buffer is automatically updated

//     while (slave.available()) {
//         // show received data
//         for (size_t i = 0; i < BUFFER_SIZE; ++i) {
//             printf("%d ", spi_slave_rx_buf[i]);
//         }
//         printf("\n");

//         slave.pop();
//     }
// }