def gets_current_covid19_data():
    """This function gets current covid19 data from the site disease.sh
    * Disease is an open API for disease-related statistics"""
    
    import requests
    from bs4 import BeautifulSoup
    import json

    url = "https://disease.sh/v3/covid-19/all"
    response = requests.get(url)
    
    data = response.json()
    print(data)

    with open('./Covid19_data/Entire_world_covid_data.json', 'w') as outfile:
        json.dump(data, outfile)
    
    
gets_current_covid19_data()
    



