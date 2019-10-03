
//Libraries
#include <ThingSpeak.h>
#include "ESP8266WiFi.h"
#include <DHT.h>;
#include <Wire.h>
#include "MutichannelGasSensor.h"
#include <SDS011.h>


//Constants
#define DHTPIN D5    // what pin we're connected to
#define DHTTYPE DHT22   // DHT 22  (AM2302)
#define node_RX D4
#define node_TX D6
#define ADDR_I2C 0x04
#define LED D0
SDS011 my_sds;
DHT dht(DHTPIN, DHTTYPE); //// Initialize DHT sensor for normal 16mhz Arduino
unsigned long Channel_ID = 864148;
char API_KEY[] = "UKQQPFB6U0R8V4US";
char ssid[] = "JioFi_20E7D6C";
char psswd[] = "2wufpbqmx0";
//char ssid[] = "MG5";
//char psswd[] = "drowssap";
WiFiClient  client;

//Variables
int chk, error;
float hum, temp, p10, p25, c;

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

    c = gas.measure_NO2();
    Serial.print("The concentration of NO2 is ");
    if(c>=0) Serial.print(c);
    else Serial.print("invalid");
    Serial.println(" ppm");
    ThingSpeak.setField(4, c);

    c = gas.measure_NH3();
    Serial.print("The concentration of NH3 is ");
    if(c>=0) Serial.print(c);
    else Serial.print("invalid");
    Serial.println(" ppm");
    ThingSpeak.setField(5, c);



    error = my_sds.read(&p25, &p10);
    if (!error) {
      Serial.println("P2.5: " + String(p25) + "\t" + "P10:  " + String(p10));
      ThingSpeak.setField(6, p25);
      ThingSpeak.setField(7, p10);
    }


    
    hum = dht.readHumidity();
    temp= dht.readTemperature();
    //Print temp and humidity values to serial monitor
    Serial.print("Humidity: ");
    Serial.print(hum);
    Serial.print(" %, Temp: ");
    Serial.print(temp);
    Serial.println(" Celsius");
    ThingSpeak.setField(1, hum);
    ThingSpeak.setField(2, temp);

    int response;
    if((response = ThingSpeak.writeFields(Channel_ID, API_KEY)) == 200) {
      Serial.println("Data updaated successfully!");
    }
    else {
      Serial.println("Problem Updating channel!\nError code: " + String(response)); 
    }
    delay(15000); //Delay 15 sec.
    Serial.println("...\n\n\n\n\n\n\n");
}
