import csv
data = {}
teams = {}


def teams_reset():
    teams = {
        'hum': {
            1: -1,
            # 45: -1,
            6: -1,
            # 20: -1,
            11: -1
        },
        'temp': {
            1: -1,
            # 45: -1,
            6: -1,
            # 20: -1,
            11: -1
        },
        'co': {
            1: -1,
            # 45: -1,
            6: -1,
            # 20: -1,
            11: -1
        },
        'no2': {
            1: -1,
            # 45: -1,
            6: -1,
            # 20: -1,
            11: -1
        },
        'h2': {
            1: -1,
            # 45: -1,
            6: -1,
            # 20: -1,
            11: -1
        },
        'pm25': {
            1: -1,
            # 45: -1,
            6: -1,
            # 20: -1,
            11: -1
        },
        'pm10': {
            1: -1,
            # 45: -1,
            6: -1,
            # 20: -1,
            11: -1
        }
    }
    return teams


# team_styles = {
#     11: {
#         'clr': 'red',
#         'sty': '-'
#     },
#     1: {
#         'clr': 'blue',
#         'sty': '--'
#     },
#     20: {
#         'clr': 'black',
#         'sty': ':'
#     },
#     6: {
#         'clr': 'brown',
#         'sty': '-.'
#     },
#     45: {
#         'clr': 'yellow',
#         'sty': '-'
#     }
# }
team_numbers = [6, 11, 1]
# team_numbers = [6, 1, 45, 20, 11]

for i in team_numbers:
    print("Reading " + str(i) +".csv...")
    with open(str(i)+".csv") as file:
        csv_data = csv.reader(file, delimiter=',')
        for row in csv_data:
            if(row[0] == 'created_at'):
                continue
            if row[0] not in data:
                data[row[0]] = teams_reset()
            data[row[0]]['hum'][i] = row[2]
            data[row[0]]['temp'][i] = row[3]
            data[row[0]]['co'][i] = row[4]
            data[row[0]]['no2'][i] = row[5]
            data[row[0]]['h2'][i] = row[6]
            data[row[0]]['pm10'][i] = row[8]
            data[row[0]]['pm25'][i] = row[7]
    print("Read!")

time = sorted(data.keys())
print("Sorting Output!")
for i in range(len(time)):
    for j in team_numbers:
        if(data[time[i]]['hum'][j] == -1):
            k = i-1
            while(data[time[k]]['hum'][j] == -1):
                k = k-1
            data[time[i]]['hum'][j] = data[time[k]]['hum'][j]
        if(data[time[i]]['temp'][j] == -1):
            k = i-1
            while(data[time[k]]['temp'][j] == -1):
                k = k-1
            data[time[i]]['temp'][j] = data[time[k]]['temp'][j]
        if(data[time[i]]['co'][j] == -1):
            k = i-1
            while(data[time[k]]['co'][j] == -1):
                k = k-1
            data[time[i]]['co'][j] = data[time[k]]['co'][j]
        if(data[time[i]]['no2'][j] == -1):
            k = i-1
            while(data[time[k]]['no2'][j] == -1):
                k = k-1
            data[time[i]]['no2'][j] = data[time[k]]['no2'][j]
        if(data[time[i]]['h2'][j] == -1):
            k = i-1
            while(data[time[k]]['h2'][j] == -1):
                k = k-1
            data[time[i]]['h2'][j] = data[time[k]]['h2'][j]
        if(data[time[i]]['pm25'][j] == -1):
            k = i-1
            while(data[time[k]]['pm25'][j] == -1):
                k = k-1
            data[time[i]]['pm25'][j] = data[time[k]]['pm25'][j]
        if(data[time[i]]['pm10'][j] == -1):
            k = i-1
            while(data[time[k]]['pm10'][j] == -1):
                k = k-1
            data[time[i]]['pm10'][j] = data[time[k]]['pm10'][j]
print("Done! Generating output...")

final = "time"
for i in team_numbers:
    final = final + ',hum' + str(i)
    final = final + ',temp' + str(i)
    final = final + ',co' + str(i)
    final = final + ',no2' + str(i)
    final = final + ',h2' + str(i)
    final = final + ',pm25' + str(i)
    final = final + ',pm10' + str(i)
final = final + "\n"

for j in sorted(data.keys()):
    final = final + j + ','
    for i in team_numbers:
        final = final + str(data[j]['hum'][i]) + ','
        final = final + str(data[j]['temp'][i]) + ','
        final = final + str(data[j]['co'][i]) + ','
        final = final + str(data[j]['no2'][i]) + ','
        final = final + str(data[j]['h2'][i]) + ','
        final = final + str(data[j]['pm25'][i]) + ','
        final = final + str(data[j]['pm10'][i]) + ','
    final = final + "\n"
print("Done!")
with open('final.csv', 'x') as file:
    file.write(final)
