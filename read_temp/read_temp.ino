#include <Adafruit_CircuitPlayground.h>

float tempC, tempF;

void setup() {
  Serial.begin(9600);
  CircuitPlayground.begin();
}

void loop() {
  tempC = CircuitPlayground.temperature();
  tempF = CircuitPlayground.temperatureF();

  Serial.print("C: ");
  Serial.print(tempC);
  Serial.print("F: ");
  Serial.println(tempF);

  delay(1000);
}
