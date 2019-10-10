from OneM2M import *

server = 'http://127.0.0.1:8080'
cse = '/~/in-cse/in-name/'
ae = 'Outdoor_Air_pollution_mobile_6'
containers = ["DHT22", "SDS011", "Grove_Gas", "GPS"]

print(register_ae(server+cse, ae, ['team_6', 'Sachin Chaudary', 'Rajashekar Reddy']))

for i in containers:
    print(create_cnt(server+cse+ae, i))