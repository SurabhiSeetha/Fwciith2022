//----------------------Skeleton Code--------------------//
#include <WiFi.h>
#include <WiFiUdp.h>
#include <ArduinoOTA.h>
#include<Arduino.h>
//    Can be client or even host   //
#ifndef STASSID
#define STASSID "Vijay"  // Replace with your network credentials
#define STAPSK  "8143738448"
#endif

const char* ssid = STASSID;
const char* password = STAPSK;


void OTAsetup() {
  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);
  while (WiFi.waitForConnectResult() != WL_CONNECTED) {
    delay(5000);
    ESP.restart();
  }
  ArduinoOTA.begin();
}

void OTAloop() {
  ArduinoOTA.handle();
}
bool X,Y,Z,W,F;
void setup()
{
	otasetup();
pinMode(22,OUTPUT);
}
void loop()
{
	otaloop();
X=1;
Y=1;
Z=1;
W=1; 
F=(X&&!Y)||(X&&W)||(Y&&Z)||(Z&&!W);
digitalWrite(22,F);
}
