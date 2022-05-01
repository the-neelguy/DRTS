

#include <SimpleDHT.h>

char d;
#include "DHT.h"

#define DHTPIN 7    

#define DHTTYPE DHT11

DHT dht(DHTPIN, DHTTYPE);


int PULSE_INPUT = 0;

void setup() 
{
  Serial.begin(9600);
   pinMode(13, OUTPUT);
 
  dht.begin();
}

void loop() {
  if(Serial.available())
  {
    d=Serial.read();
  }
  if (d=='t')
  {
  
    byte humidity = dht.readHumidity();
    byte temperature = dht.readTemperature();
    Serial.println(temperature);
    Serial.println(humidity);
    delay(1500);
  }
  if (d=='a')
  {
    int myBPM = analogRead(PULSE_INPUT); 
    int npulse = myBPM/4;  
      Serial.println(npulse);
      delay(1000); 
  }
  if (d=='l')
  {
    digitalWrite(13, HIGH);   
  }
  if (d=='o')
  {
    digitalWrite(13,LOW);
  }
}
