
//Libraries
#include <ThingSpeak.h>
#include "ESP8266WiFi.h"
#include "DHT.h";
#include <Wire.h>
#include "MutichannelGasSensor.h"
#include <SDS011.h>
#include <ESP8266HTTPClient.h>
#include <stdlib.h>
#include <SoftwareSerial.h>
#include <TinyGPS.h>


//Constants
#define DHT_22 0
#define SDS 11
#define GROVE 2
#define GPS 3
#define DHTPIN D4    // what pin we're connected to
#define DHTTYPE DHT22   // DHT 22  (AM2302)
#define node_RX D5
#define node_TX D6
#define ADDR_I2C 0x04
#define LED D0
#define gps_RX D7
#define gps_TX D3
TinyGPS gps;
SoftwareSerial ss(gps_TX, gps_RX);
SDS011 my_sds;
DHT dht(DHTPIN, DHTTYPE); //// Initialize DHT sensor for normal 16mhz Arduino
unsigned long Channel_ID = 864148;
char API_KEY[] = "UKQQPFB6U0R8V4US";
//char ssid[] = "JioFi_20E7D6C";
//char psswd[] = "2wufpbqmx0";
//char ssid[] = "MG5";
//char psswd[] = "drowssap";
char ssid[] = "Nitro 5";
char psswd[] = "wvZu69eF";
WiFiClient  client;

//Variables
int chk, error;
float hum, temp, p10, p25, c, flat, flon;
String dht_22, sds, gas_val, gps_val;
unsigned long age;

//ONEM2M
int post(String data, int Sensor_type) {
  String server = "http://10.1.129.146:8080";
  String cse = "/~/in-cse/in-name/";
  String ae = "Outdoor_Air_pollution_mobile_6/";
  String container;
  if(Sensor_type == DHT_22) container = "DHT22";
  else if(Sensor_type == SDS) container = "SDS011";
  else if(Sensor_type == GROVE) container = "Grove_Gas";
  else if(Sensor_type == GPS) container = "GPS";

  char m2m[200];
  String Data;
  Data = "{\"m2m:cin\": {"
    "\"con\":\"" + data + "\""
    "}}";
  HTTPClient http;
  http.begin(server+cse+ae+container);
  http.addHeader("X-M2M-Origin", "admin:admin");
  http.addHeader("Content-type", "application/json;ty=4");
  int response = http.POST(Data);
  http.end();
  return response;
}
void update(int val, String sensor) {
  if(val == 201) Serial.print(sensor + " values updated successfully\n");
  else Serial.print("There was an error while uploading " + sensor +" values");
}

static void smartdelay(unsigned long ms) {
  unsigned long start = millis();
  do {
    while (ss.available())
      gps.encode(ss.read());
  } while (millis() - start < ms);
}

static void print_float(float val, float invalid, int len, int prec) {
  if (val == invalid) {
    while (len-- > 1)
      Serial.print('*');
    Serial.print(' ');
  }
  else{
    Serial.print(val, prec);
    int vi = abs((int)val);
    int flen = prec + (val < 0.0 ? 2 : 1); // . and -
    flen += vi >= 1000 ? 4 : vi >= 100 ? 3 : vi >= 10 ? 2 : 1;
    for (int i=flen; i<len; ++i)
      Serial.print(' ');
  }
  smartdelay(0);
}

void setup()
{
  pinMode(LED, OUTPUT);
  Serial.begin(115200);
  dht.begin();
  my_sds.begin(node_RX, node_TX);
  gas.begin(ADDR_I2C);
  gas.powerOn(); 
  Serial.println("Let's begin!");
  WiFi.mode(WIFI_STA);
  WiFi.disconnect();
  ThingSpeak.begin(client);
  digitalWrite(LED, HIGH);
  ss.begin(9600);
}


void loop()
{
     if(WiFi.status() != WL_CONNECTED){
      digitalWrite(LED, HIGH);
      Serial.print("Attempting to connect to SSID: ");
      Serial.print(ssid); 
      Serial.println(" with password: " + String(psswd));
      while(WiFi.status() != WL_CONNECTED){
        WiFi.begin(ssid, psswd);  // Connect to WPA/WPA2 network. Change this line if using open or WEP network
        Serial.print(".");
        delay(5000);     
      } 
      Serial.println("\nConnected.");
      digitalWrite(LED, LOW);
    }
    
    c = gas.measure_CO();
    Serial.print("The concentration of CO is ");
    if(c>=0) Serial.print(c);
    else Serial.print("invalid");
    Serial.println(" ppm");
    ThingSpeak.setField(3, c);
    gas_val = String(c) + ",";
    
    c = gas.measure_NO2();
    Serial.print("The concentration of NO2 is ");
    if(c>=0) Serial.print(c);
    else Serial.print("invalid");
    Serial.println(" ppm");
    ThingSpeak.setField(4, c);
    gas_val = gas_val + String(c) + ",";

    c = gas.measure_NH3();
    Serial.print("The concentration of NH3 is ");
    if(c>=0) Serial.print(c);
    else Serial.print("invalid");
    Serial.println(" ppm");
    ThingSpeak.setField(5, c);
    gas_val = gas_val + String(c);


    error = my_sds.read(&p25, &p10);
    if (!error) {
      Serial.println("P2.5: " + String(p25) + "\t" + "P10:  " + String(p10));
      ThingSpeak.setField(6, p25);
      ThingSpeak.setField(7, p10);
      sds = String(p25) + "," + String(p10);
      
    }
    
    hum = dht.readHumidity();
    temp= dht.readTemperature();

//    Print temp and humidity values to serial monitor
    Serial.print("Humidity: ");
    Serial.print(hum);
    Serial.print(" %, Temp: ");
    Serial.print(temp);
    Serial.println(" Celsius");
    ThingSpeak.setField(1, hum);
    ThingSpeak.setField(2, temp);
    dht_22 = String(hum) + "," + String(temp);

    gps.f_get_position(&flat, &flon, &age);
    print_float(flat, TinyGPS::GPS_INVALID_F_ANGLE, 10, 6);
    print_float(flon, TinyGPS::GPS_INVALID_F_ANGLE, 11, 6);
    Serial.println();
    gps_val = String(flat) + ',' + String(flon);

    smartdelay(1000);
    
//    update(post(dht_22, DHT_22), "DHT22");
//    update(post(sds, SDS), "SDS011");
//    update(post(gas_val, GROVE), "Grove Gas sensor");
//    update(post(gps_val, GPS), "GPS");
//    int response;
//    if((response = ThingSpeak.writeFields(Channel_ID, API_KEY)) == 200) {
//      Serial.println("Data updated successfully!");
//    }
//    else {
//      Serial.println("Problem Updating channel!\nError code: " + String(response)); 
//    }
    delay(15000); //Delay 15 sec.
    Serial.println("...\n\n\n\n\n\n\n");
}
