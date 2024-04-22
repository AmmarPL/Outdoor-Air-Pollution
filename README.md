# Embedded System for Air Quality Measurement

This project involves the design and implementation of an embedded system to measure air quality, with a focus on particulate matter (PM10) concentrations. It was specifically developed and tested during Diwali in 2019, when air pollution levels are known to spike significantly due to fireworks and other festivities.

# Overview
The air quality measurement device uses an ESP8266 microcontroller to gather data from various sensors and transmit it to a Python Flask server using oneM2M. The data is then visualized and analyzed through Thingspeak, showcasing significant spikes in PM10 levels, particularly around student residential areas. The entire circuit was designed using EagleCAD.

# Features
Sensor Integration: Incorporates multiple sensors to measure various pollutants, with a focus on PM10 particulate matter.

Connectivity: Uses an ESP8266 microcontroller for processing sensor data and providing Wi-Fi connectivity.
<img width="592" alt="image" src="https://github.com/AmmarPL/Outdoor-Air-Pollution/assets/46021351/1aa5a4be-ac97-4041-966d-a729af800239">


Data Handling: Transmits data to a Python Flask server, which is then pushed to Thingspeak for analysis and visualization.
<img width="1040" alt="image" src="https://github.com/AmmarPL/Outdoor-Air-Pollution/assets/46021351/9b75351a-7413-40e7-af59-7a0f37356236">


EagleCAD Design: Custom PCB design for neatly organized and efficient sensor integration and microcontroller setup.
<img width="1037" alt="image" src="https://github.com/AmmarPL/Outdoor-Air-Pollution/assets/46021351/0a17022b-2493-4de0-b96c-0f14a7c32f71">


# Results
We found that some of the air quality indicators had a bad spike around Diwali.
<img width="332" alt="image" src="https://github.com/AmmarPL/Outdoor-Air-Pollution/assets/46021351/da802338-fe0a-4765-bea2-e13a00feab46">

We also found that these spikes were concentrated around the student residences. 
<img width="797" alt="image" src="https://github.com/AmmarPL/Outdoor-Air-Pollution/assets/46021351/d2248ce1-97d8-4a18-b08b-9c988d08bad0">

Both these plots are for PM10, but similar spikes were found in PM2.5 and CO, but not with NH3 and NO2.


