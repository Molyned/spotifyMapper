import importlib
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import re
import pandas as pd
import os
import requests
from lxml import html
import config
import geocoder
import json
import pandas

jsonArray, objArray, lngData, latData = [], [], [], []

def spotifyLogIn():
    spotifyInfo = {
        "username": config.username,
        "password": config.password,
        "recaptcha-token": config.recaptchaToken
    }

    sessionReq = requests.session()
    loginPage = 'https://accounts.spotify.com/en/login?continue=https:%2F%2Fopen.spotify.com%2Fbrowse%2Ffeatured'
    login = sessionReq.get(loginPage)
    tree = html.fromstring(login.text)
    authenToken = list(set(tree.xpath("//input[@id='recaptcha-token']/@value")))

    login = sessionReq.post(
        loginPage,
        data = spotifyInfo,
        headers = dict(referer=loginPage)
    )
    return 0
def scrapeCities():
    drakeURL = 'https://open.spotify.com/artist/7n2wHs1TKAczGzO7Dd2rGr/about' #'https://open.spotify.com/artist/3TVXtAsR1Inumwj472S9r4/about'
    urlList = ['https://open.spotify.com/artist/7n2wHs1TKAczGzO7Dd2rGr/about',
            'https://open.spotify.com/artist/4nDoRrQiYLoBzwC5BhVJzF/about']
            # 'https://open.spotify.com/artist/246dkjvS1zLTtiykXe5h60/about',
            # 'https://open.spotify.com/artist/06HL4z0CvFAxyc27GXpf02/about',
            # 'https://open.spotify.com/artist/1sBkRIssrMs1AbVkOJbc7a/about',
            # 'https://open.spotify.com/artist/66CXWjxzNUsdJxJ2JdwvnR/about',
            # 'https://open.spotify.com/artist/6eUKZXaKkcviH0Ku9w2n3V/about',
            # 'https://open.spotify.com/artist/6LuN9FCkKOj5PcnpouEgny/about',
            # 'https://open.spotify.com/artist/1uNFoZAHBGtllmzznpCI3s/about',
            # 'https://open.spotify.com/artist/7jVv8c5Fj3E9VhNjxT4snq/about',
            # 'https://open.spotify.com/artist/60rpJ9SgigSd16DOAG7GSa/about',
            # 'https://open.spotify.com/artist/7bXgB6jMjp9ATFy66eO08Z/about',
            # 'https://open.spotify.com/artist/6l3HvQ5sa6mXTsMTB19rO5/about',
            # 'https://open.spotify.com/artist/0Y5tJX1MQlPlqiwlOH1tJY/about',
            # 'https://open.spotify.com/artist/69GGBxA162lTqCwzJG5jLp/about',
            # 'https://open.spotify.com/artist/6qqNVTkY8uBg9cP3Jd7DAH/about',
            # 'https://open.spotify.com/artist/2wY79sveU1sp5g7SokKOiI/about',
            # 'https://open.spotify.com/artist/0hCNtLu0JehylgoiP8L4Gh/about',
            # 'https://open.spotify.com/artist/3JhNCzhSMTxs9WLGJJxWOY/about',
            # 'https://open.spotify.com/artist/23fqKkggKUBHNkbKtXEls4/about',
            # 'https://open.spotify.com/artist/0du5cEVh5yTK9QJze8zA0C/about',
            # 'https://open.spotify.com/artist/04gDigrS5kc9YWfZHwBETP/about',
            # 'https://open.spotify.com/artist/5pKCCKE2ajJHZ9KAiaK11H/about',
            # 'https://open.spotify.com/artist/4VMYDCV2IEDYJArk749S6m/about',
            # 'https://open.spotify.com/artist/4gzpq5DPGxSnKTe4SA8HAU/about',
            # 'https://open.spotify.com/artist/6deZN1bslXzeGvOLaLMOIF/about',
            # 'https://open.spotify.com/artist/4dpARuHxo51G3z768sgnrY/about',
            # 'https://open.spotify.com/artist/1Xyo4u8uXC1ZmMpatF05PJ/about',
            # 'https://open.spotify.com/artist/3gd8FJtBJtkRxdfbTu19U2/about',
            # 'https://open.spotify.com/artist/20sxb77xiYeusSH8cVdatc/about',
            # 'https://open.spotify.com/artist/55Aa2cqylxrFIXC767Z865/about',
            # 'https://open.spotify.com/artist/17lzZA2AlOHwCwFALHttmp/about',
            # 'https://open.spotify.com/artist/0YMeriqrS3zgsX24nfY0F0/about',
            # 'https://open.spotify.com/artist/2YZyLoL8N0Wb9xBt1NhZWg/about',
            # 'https://open.spotify.com/artist/4V8LLVI7PbaPR0K2TGSxFF/about',
            # 'https://open.spotify.com/artist/0LcJLqbBmaGUft1e9Mm8HV/about',
            # 'https://open.spotify.com/artist/5K4W6rqBFWDnAN6FQUkS6x/about',
            # 'https://open.spotify.com/artist/3jK9MiCrA42lLAdMGUZpwa/about',
            # 'https://open.spotify.com/artist/08yf5A2nS4XEeNvabDXqyg/about',
            # 'https://open.spotify.com/artist/4UXqAaa6dQYAk18Lv7PEgX/about',
            # 'https://open.spotify.com/artist/7dGJo4pcD2V6oG8kP0tJRR/about',
            # 'https://open.spotify.com/artist/2o5jDhtHVPhrJdv3cEQ99Z/about',
            # 'https://open.spotify.com/artist/1vyhD5VmyZ7KMfW5gqLgo5/about',
            # 'https://open.spotify.com/artist/540vIaP2JwjQb9dm3aArA4/about',
            # 'https://open.spotify.com/artist/0EmeFodog0BfCgMzAIvKQp/about',
            # 'https://open.spotify.com/artist/1vCWHaC5f2uS3yhpwWbIA6/about',
            # 'https://open.spotify.com/artist/77AiFEVeAVj2ORpC85QVJs/about',
            # 'https://open.spotify.com/artist/6cEuCEZu7PAE9ZSzLLc2oQ/about',
            # 'https://open.spotify.com/artist/2XnBwblw31dfGnspMIwgWz/about',
            # 'https://open.spotify.com/artist/1Cs0zKBU1kc0i8ypK3B9ai/about',
            # 'https://open.spotify.com/artist/64KEffDW9EtZ1y2vBYgq8T/about',
            # 'https://open.spotify.com/artist/0C0XlULifJtAgn6ZNCW2eu/about',
            # 'https://open.spotify.com/artist/7jy3rLJdDQY21OgRLCZ9sD/about',
            # 'https://open.spotify.com/artist/1dfeR4HaWDbWqFHLkxsg1d/about',
            # 'https://open.spotify.com/artist/3WrFJ7ztbogyGnTHbHJFl2/about',]

    
    # # create a new Firefox session
    # driver = webdriver.Firefox()
    # driver.implicitly_wait(30)
    # driver.get(drakeURL)

    # python_button = driver.find_element_by_class_name('ArtistAbout__city__name') 
    # # python_button.click()
    
    pageData = requests.get(drakeURL, timeout = 5)
    scraper = BeautifulSoup(pageData.content, 'html.parser')# (driver.page_source, 'lxml') #
    mainText = scraper.find_all('script')[5]
    mainTextString = str(mainText)
    global locationData
    locationData = mainTextString.split("cities", 1)[1] 
    
    # for aboutPage in urlList: 
    #     pageData = requests.get(aboutPage, timeout = 5)
    #     scraper = BeautifulSoup(pageData.content, 'html.parser')# (driver.page_source, 'lxml') #
    #     mainText = scraper.find_all('script')[5]
    #     mainTextString = str(mainText)
    #     locationData = mainTextString.split("cities", 1)[1] 
    #     # driver.close()
    return locationData

def dataCleaner(locationData):
    cleanedString = locationData[locationData.index("[")+1:locationData.index("]")]
    cityArray = cleanedString.split(',{')
    print(cleanedString)
    for i in range(len(cityArray)):
        if i == 0:
            cityArray[i] = cityArray[i]
        else:
            cityArray[i] = "{" + cityArray[i]
        jsonArray.append(cityArray[i])

    for dataCell in jsonArray:
        jsonCell = json.loads(dataCell)
        objArray.append(jsonCell)
    return objArray, 

def geolocator(objArray):
    for x in objArray:
        try:
            streamingLoc = x['country'] +', ' + x['city']
            g = geocoder.arcgis(streamingLoc)
            lng = g.json['lng']
            lat = g.json['lat']
        except:
            lng =  'n/a'
            lat =  'n/a'
        latData.append(lat)
        lngData.append(lng)
    print(latData)
    print(lngData)

def main():
    # spotifyLogIn()
    scrapeCities()
    dataCleaner(locationData)
    # geolocator(objArray)

if __name__ == '__main__':
    main()