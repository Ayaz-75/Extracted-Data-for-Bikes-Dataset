from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import requests
import time as t

all_names = []
all_prices = []
all_cities = []
all_years = []
all_kilometers = []

for i in range(1, 20):
    web_url = 'https://www.pakwheels.com/used-bikes/search/-/ct_karachi/110/pr_110000_More/?page='+str(i)

    # response = requests.get(web_url)
    # print(response.status_code)


    path = 'C:\Development\chromedriver'

    options = Options()
    # options.headless = True

    service = Service(executable_path = path)
    driver = webdriver.Chrome(service = service, options=options)

    driver.get(web_url)

    details_container = driver.find_elements(by='xpath', value='//div[@class="col-md-9 grid-style"]')
    # all_other_details = driver.find_elements(by='xpath', value='//div[@class="col-md-12 grid-date"]')

    for name in details_container:
        t.sleep(5)
        name_string = name.find_element(by='xpath', value='./div/div/div/a/h3')
        price = name.find_element(by='xpath', value='./div/div/div/div/div')
        city = name.find_element(by='xpath', value='./div[2]/div/ul[1]')
        year = name.find_element(by='xpath', value='./div[2]/div/ul[2]/li[1]')
        kilo = name.find_element(by='xpath', value='./div[2]/div/ul[2]/li[2]')
        
        all_names.append(name_string.text.strip())
        all_prices.append(price.text.strip())
        all_cities.append(city.text.strip())
        all_years.append(year.text.strip())
        all_kilometers.append(kilo.text.strip())





print(all_names)
print(len(all_names))
print(all_prices)
print(len(all_prices))
print(all_cities)
print(len(all_cities))
print(all_years)
print(len(all_years))
print(all_kilometers)
print(len(all_kilometers))


import pandas as pd
data_dict = {
    'Bike names ': all_names,
    'Bike Prices': all_prices,
    'City in': all_cities,
    'Model Year': all_years,
    'Kilometers ran': all_kilometers

}

df = pd.DataFrame(data_dict)
try:
    df.to_csv('football_headlines.csv', index=False)
except:
    FileExistsError()

    # for each in all_other_details:
    #     city = each.find_element(by='xpath', value='./ul/li')
    #     year = each.find_element(by='xpath', value='')




# print(len(all_names))
# //div[@class='col-md-12 grid-date']/ul

# /div/div/div/div/div
#//div[@class='col-md-9 grid-style']/div/div/div/a/h3