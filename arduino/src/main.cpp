#include <Arduino.h>


const int pResistor = A0; // Photoresistor at Arduino analog pin A0
const int ledPin=9;       // Led pin at Arduino pin 9

//Variables
int value;				  // Store value from photoresistor (0-1023)

void setup() {
  Serial.begin(9600);
  pinMode(pResistor, INPUT);// Set pResistor - A0 pin as an input (optional)
}

void loop() {
  // BLINK CODE
  // digitalWrite(LED_BUILTIN, HIGH);  // turn the LED on (HIGH is the voltage level)
  // delay(1000);                      // wait for a second
  // digitalWrite(LED_BUILTIN, LOW);   // turn the LED off by making the voltage LOW
  // delay(1000);                      // wait for a second

  value = analogRead(pResistor);
  
  Serial.println(value);

}