import csv
import matplotlib.pyplot as plt

time = []
temp = []
hum = []
h2 = []
no2 = []
co = []
pm10 = []
pm25 = []

print("Reading data file")
with open('feeds.csv') as file:
    csvData = csv.reader(file, delimiter=',')
    for row in csvData:
        time.append(row[0])
        hum.append(row[2])
        temp.append(row[3])
        co.append(row[4])
        no2.append(row[5])
        h2.append(row[6])
        pm25.append(row[7])
        pm10.append(row[8])
print("Reading complete")
time.remove(time[0])
hum.remove(hum[0])
temp.remove(temp[0])
co.remove(co[0])
no2.remove(no2[0])
h2.remove(h2[0])
pm25.remove(pm25[0])
pm10.remove(pm10[0])

temp = [round(float(x), 2) for x in temp]
hum = [round(float(x), 2) for x in hum]
co = [round(float(x), 2) for x in co]
no2 = [round(float(x), 2) for x in no2]
h2 = [round(float(x), 2) for x in h2]
pm25= [round(float(x), 2) for x in pm25]
pm10 = [round(float(x), 2) for x in pm10]

print("Plotting Temperature")
plt.xlabel('Temperature')
plt.ylabel('Date')
plt.plot(temp, time)
plt.title('Temp vs Time')
plt.savefig('Temp.png', format='png')
plt.show()
print("Plotting Complete")

print("Plotting Humidity")
plt.xlabel('Humidity')
plt.ylabel('Date')
plt.plot(hum, time)
plt.title('Hum vs Time')
plt.savefig('Hum.png', format='png')
plt.show()
print("Plotting Complete")

print("Plotting CO")
plt.xlabel('CO')
plt.ylabel('Date')
plt.plot(co, time)
plt.title('CO vs Time')
plt.savefig('CO.png', format='png')
plt.show()
print("Plotting Complete")

print("Plotting NO2")
plt.xlabel('NO2')
plt.ylabel('Date')
plt.plot(no2, time)
plt.title('NO2 vs Time')
plt.savefig('NO2.png', format='png')
plt.show()
print("Plotting Complete")

print("Plotting H2")
plt.xlabel('H2')
plt.ylabel('Date')
plt.plot(h2, time)
plt.title('H2 vs Time')
plt.savefig('H2.png', format='png')
plt.show()
print("Plotting Complete")

print("Plotting PM2.5")
plt.xlabel('PM2.5')
plt.ylabel('Date')
plt.plot(pm25, time)
plt.title('PM2.5 vs Time')
plt.savefig('PM25.png', format='png')
plt.show()
print("Plotting Complete")

print("Plotting PM10")
plt.xlabel('PM10')
plt.ylabel('Date')
plt.plot(pm10, time)
plt.title('PM10 vs Time')
plt.savefig('PM10.png', format='png')
plt.show()
print("Plotting Complete")
