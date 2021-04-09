import requests
from requests import get
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

def scrap():
    url = "https://www.kct.ac.in/programmes/electrical-and-electronics-engineering/"
    headers = {"Accept-Language": "en-US, en;q=0.5"}
    results = requests.get(url, headers=headers)

    soup = BeautifulSoup(results.text, "html.parser")

    names = []
    designations = []

    staff_div = soup.find_all('div', class_='staffDetail col-lg-8 col-12')

    for container in staff_div:

        #name
        name = container.h3.text
        names.append(name)
        
        #designation
        designation = container.p.text
        designations.append(designation)

        #building pandas

    staffs = pd.DataFrame({
        'name': names,'designation': designations
        })

    #print(staffs)
    return names,designations

#staffs.to_csv('staffs.csv')
