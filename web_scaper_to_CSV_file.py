import requests
import csv
import json

url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'

# send request to download the file
response = requests.get(url)

# read content of the downloaded file
content = response.content.decode('utf-8')

# parse the CSV data
rows = csv.reader(content.splitlines())
header = next(rows)
data = {}

for row in rows:
    country = row[1]
    if country not in data:
        data[country] = {}
    for i in range(4, len(header)):
        date = header[i]
        confirmed = int(row[i])
        if date not in data[country]:
            data[country][date] = confirmed
        else:
            data[country][date] += confirmed

# save the data as JSON file
with open('covid19_data.json', 'w') as f:
    json.dump(data, f)
