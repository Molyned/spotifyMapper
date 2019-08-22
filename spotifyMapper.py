import importlib
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
# import pandas as pd
import os
import requests
from lxml import html
import config
import geocoder
import json
import pandas
import chart_studio
import chart_studio.plotly as py
import plotly.graph_objs as go
import random
import pymongo

chart_studio.tools.set_credentials_file(username=config.mapUsername, api_key=config.mapApiToken)
mapbox_access_token = config.mapAccessToken


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
    urlList = ['https://open.spotify.com/artist/7n2wHs1TKAczGzO7Dd2rGr/about',
            'https://open.spotify.com/artist/0YMeriqrS3zgsX24nfY0F0/about',
            'https://open.spotify.com/artist/4nDoRrQiYLoBzwC5BhVJzF/about',
            'https://open.spotify.com/artist/2pKYAosUpmrLvvl0Ss211W/about',
            'https://open.spotify.com/artist/246dkjvS1zLTtiykXe5h60/about',
            'https://open.spotify.com/artist/06HL4z0CvFAxyc27GXpf02/about',
            'https://open.spotify.com/artist/3TVXtAsR1Inumwj472S9r4/about',
            'https://open.spotify.com/artist/66CXWjxzNUsdJxJ2JdwvnR/about',
            'https://open.spotify.com/artist/6eUKZXaKkcviH0Ku9w2n3V/about',
            'https://open.spotify.com/artist/6LuN9FCkKOj5PcnpouEgny/about',
            'https://open.spotify.com/artist/1uNFoZAHBGtllmzznpCI3s/about',
            'https://open.spotify.com/artist/7jVv8c5Fj3E9VhNjxT4snq/about',
            'https://open.spotify.com/artist/60rpJ9SgigSd16DOAG7GSa/about',
            'https://open.spotify.com/artist/7bXgB6jMjp9ATFy66eO08Z/about',
            'https://open.spotify.com/artist/6l3HvQ5sa6mXTsMTB19rO5/about',
            'https://open.spotify.com/artist/0Y5tJX1MQlPlqiwlOH1tJY/about',
            'https://open.spotify.com/artist/69GGBxA162lTqCwzJG5jLp/about',
            'https://open.spotify.com/artist/6qqNVTkY8uBg9cP3Jd7DAH/about',
            'https://open.spotify.com/artist/2wY79sveU1sp5g7SokKOiI/about',
            'https://open.spotify.com/artist/0hCNtLu0JehylgoiP8L4Gh/about',
            'https://open.spotify.com/artist/3JhNCzhSMTxs9WLGJJxWOY/about',
            'https://open.spotify.com/artist/23fqKkggKUBHNkbKtXEls4/about',
            'https://open.spotify.com/artist/0du5cEVh5yTK9QJze8zA0C/about',
            'https://open.spotify.com/artist/04gDigrS5kc9YWfZHwBETP/about',
            'https://open.spotify.com/artist/5pKCCKE2ajJHZ9KAiaK11H/about',
            'https://open.spotify.com/artist/4VMYDCV2IEDYJArk749S6m/about',
            'https://open.spotify.com/artist/4gzpq5DPGxSnKTe4SA8HAU/about',
            'https://open.spotify.com/artist/6deZN1bslXzeGvOLaLMOIF/about',
            'https://open.spotify.com/artist/4dpARuHxo51G3z768sgnrY/about',
            'https://open.spotify.com/artist/1Xyo4u8uXC1ZmMpatF05PJ/about',
            'https://open.spotify.com/artist/3gd8FJtBJtkRxdfbTu19U2/about',
            'https://open.spotify.com/artist/20sxb77xiYeusSH8cVdatc/about',
            'https://open.spotify.com/artist/55Aa2cqylxrFIXC767Z865/about',
            'https://open.spotify.com/artist/17lzZA2AlOHwCwFALHttmp/about',
            'https://open.spotify.com/artist/2YZyLoL8N0Wb9xBt1NhZWg/about',
            'https://open.spotify.com/artist/4V8LLVI7PbaPR0K2TGSxFF/about',
            'https://open.spotify.com/artist/0LcJLqbBmaGUft1e9Mm8HV/about',
            'https://open.spotify.com/artist/5K4W6rqBFWDnAN6FQUkS6x/about',
            'https://open.spotify.com/artist/3jK9MiCrA42lLAdMGUZpwa/about',
            'https://open.spotify.com/artist/08yf5A2nS4XEeNvabDXqyg/about',
            'https://open.spotify.com/artist/4UXqAaa6dQYAk18Lv7PEgX/about',
            'https://open.spotify.com/artist/7dGJo4pcD2V6oG8kP0tJRR/about',
            'https://open.spotify.com/artist/2o5jDhtHVPhrJdv3cEQ99Z/about',
            'https://open.spotify.com/artist/1vyhD5VmyZ7KMfW5gqLgo5/about',
            'https://open.spotify.com/artist/540vIaP2JwjQb9dm3aArA4/about',
            'https://open.spotify.com/artist/1vCWHaC5f2uS3yhpwWbIA6/about',
            'https://open.spotify.com/artist/77AiFEVeAVj2ORpC85QVJs/about',
            'https://open.spotify.com/artist/6cEuCEZu7PAE9ZSzLLc2oQ/about',
            'https://open.spotify.com/artist/2XnBwblw31dfGnspMIwgWz/about',
            'https://open.spotify.com/artist/1Cs0zKBU1kc0i8ypK3B9ai/about',
            'https://open.spotify.com/artist/64KEffDW9EtZ1y2vBYgq8T/about',
            'https://open.spotify.com/artist/0C0XlULifJtAgn6ZNCW2eu/about',
            'https://open.spotify.com/artist/7jy3rLJdDQY21OgRLCZ9sD/about',
            'https://open.spotify.com/artist/1dfeR4HaWDbWqFHLkxsg1d/about',
            'https://open.spotify.com/artist/3WrFJ7ztbogyGnTHbHJFl2/about',
            'https://open.spotify.com/artist/41MozSoPIsD1dJM0CLPjZF/about',
            'https://open.spotify.com/artist/26T3LtbuGT1Fu9m0eRq5X3/about',
            'https://open.spotify.com/artist/13ubrt8QOOCPljQ2FL1Kca/about']
    locationText, artistNameList = [], []
    
    # # create a new Firefox session
    # driver = webdriver.Firefox()
    # driver.implicitly_wait(30)
    # driver.get(drakeURL)

    # python_button = driver.find_element_by_class_name('ArtistAbout__city__name') 
    # # python_button.click()
    for i in range(len(urlList)):
        pageData = requests.get(urlList[i], timeout = 5)
        scraper = BeautifulSoup(pageData.content, 'html.parser')# (driver.page_source, 'lxml') 
        scrapedText = str(scraper)
        artistName = scrapedText[scrapedText.index('/><title>')+9:scrapedText.index(' on Spotify<')]
        mainText = scraper.find_all('script')[5]
        mainTextString = str(mainText)
        locationData = mainTextString.split("cities", 1)[1] 
        locationText.append(locationData)
        artistNameList.append(artistName)
        # driver.close()
    return locationText, artistNameList

def dataCleaner(artistNameList, locationText):
    client = pymongo.MongoClient('mongodb+srv://molyned:{}@spotifycluster-6btnk.mongodb.net/test?retryWrites=true&w=majority'.format(config.MONGO_PASSWORD))
    database = client.business
    collection = database.artistInfo

    jsonArray, totalStreams, lngData, latData, cityData, streamCount, totalLatData, totalLngData, totalCityData =[], [], [], [], [], [], [], [], []
    for j in range(len(locationText)):
        locationData = locationText[j]
        cleanedString = locationData[locationData.index("[")+1:locationData.index("]")]
        # for string in cityString:
        cityStringArray = cleanedString.split(',{')
        for i in range(len(cityStringArray)):
            if i == 0:
                cityStringArray[i] = cityStringArray[i]
            else:
                cityStringArray[i] = "{" + cityStringArray[i]
            jsonCell = json.loads(cityStringArray[i])
            jsonArray.append(jsonCell)
            
            print(jsonCell)
            
            try:
                streams = 'Monthly Listeners in ' + jsonCell['city'] + ': ' +  str(jsonCell['listeners'])
                streamingLoc = jsonCell['country'] +', ' + jsonCell['city']
                g = geocoder.arcgis(streamingLoc)
                lng = g.json['lng']
                lat = g.json['lat']
            except:
                continue
                # lng =  'n/a'
                # lat =  'n/a'
                # streams = 'Monthly Listeners: ' +  str(jsonCell['listeners'])
                # streamingLoc = 'n/a'
            streamCount.append(streams)
            cityData.append(streamingLoc)
            latData.append(lat)
            lngData.append(lng)
        
        collection.insert_one({
            artistNameList[j]: [{'streamingLocation': streamCount,  
            'lat' : latData,
            'lng': lngData,
            'listeners': streamCount}]
        })

        totalStreams.append(streamCount[:])
        totalCityData.append(cityData[:])
        totalLatData.append(latData[:])
        totalLngData.append(lngData[:])
        cityData.clear()
        latData.clear()
        lngData.clear()
        streamCount.clear()
    return totalStreams, totalCityData, totalLatData, totalLngData

def colourMaker(totalStreams):
    # rgb(30, 215, 96)
    colourList = []
    for i in range(len(totalStreams)):
        colourOne = random.randint(1,256)
        colourTwo = random.randint(1,256)
        colourThree = random.randint(1,256)
        colour = (colourOne, colourTwo, colourThree)
        goodcolour = str(colour)
        realcolour = 'rgb'+goodcolour
        colourList.append((realcolour))
    return colourList

def mapPlotter(artistNameList, colourList, totalStreams, totalCityData, totalLatData, totalLngData):
    traceData = []
    for i in range(len(totalCityData)):
        trace = go.Scattermapbox(
                lat=totalLatData[i],
                lon=totalLngData[i],
                name = artistNameList[i],
                mode='markers',
                marker=dict(
                    size=10,
                    color= colourList[i],
                    opacity=0.7
                ),
                text=totalStreams[i],
                
                hoverinfo='text')
        traceData.append(trace)

    mapLayout = go.Layout(
    title="Artist's Monthly Streamers",
    autosize=True,
    hovermode='closest',
    showlegend=True,
    mapbox=dict(
        accesstoken=mapbox_access_token,
        bearing=0,
        center=dict(
            lat=38,
            lon=-94
            ),
        pitch=0,
        zoom=3,
        style='light'
        ),
    )

    fig = dict(data=traceData, layout=mapLayout)
    py.plot(fig, filename="Artist's Monthly Streamers")
    print('Done!')

def appendToCSV():
    return 0

def main():
    # spotifyLogIn()
    locationText, artistNameList = scrapeCities()
    totalStreams, totalCityData, totalLatData, totalLngData = dataCleaner(artistNameList, locationText)
    # colourList = colourMaker(totalStreams)
    # mapPlotter(artistNameList, colourList, totalStreams, totalCityData, totalLatData, totalLngData)
    # appendToCSV()

if __name__ == '__main__':
    main()