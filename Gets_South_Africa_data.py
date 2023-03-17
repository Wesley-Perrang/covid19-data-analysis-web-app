def gets_south_african_covid19_data():
    """"""
    import requests
    import csv
    import json
    import datetime

    url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'

    # Send request to download the file
    response = requests.get(url)

    # This will decode the content to strings 
    content = response.content.decode('utf-8')
    
    list_content = None

    # parse the CSV data
    rows = csv.reader(content.splitlines())

    for row in rows:
        if row[1] == "South Africa":
            list_content = row[:-1]
            
    for i in list_content:
        if i == "":
            list_content.remove(i)
    
    south_africa = {"South Africa":list_content}

    # save the data as JSON file
    with open('./Covid19_data/covid19_data.json', 'w') as f:
        json.dump(south_africa, f)

gets_south_african_covid19_data()