import pymongo
import json
import config
import pandas as pd
from datetime import date, timedelta
import plotly.graph_objects as go

import numpy as np
import matplotlib
import cufflinks as cf
import plotly
import plotly.offline as py
import plotly.graph_objs as go

cf.go_offline()

# def listCreator(city):
#     global city
#     city = []
#     return city

client = pymongo.MongoClient('mongodb+srv://molyned:{}@spotifycluster-6btnk.mongodb.net/test?retryWrites=true&w=majority'.format(config.MONGO_PASSWORD))
database = client.business
def getArtistName():
    fullDate = date.today()
    collection = database.artistInfo2[fullDate]
    myCursor = collection.find()
    for i in range(1):
        item = myCursor[i]
        artist_Name = item['name']
        artistArray = item['artist']['cities']
        for row in artistArray:
                artistCity = row['city']
        # [listCreator(x) for x in artistArray]
    global artistCityArr
    artistCityArr = []     
    return artistCityArr

def getMongoData(date):
    collection = database.artistInfo2[date]
    myCursor = collection.find()
    for item in myCursor:
        artistName = item['name']
        if artistName == 'Shawn Mendes':
            artistArray = item['artist']['cities']
            artistCity = artistArray['city']

            for row in artistArray:
                artistListener = row['listeners']
                artistCity = row['city']
                artistStreams = row['streams']
                # print(artistName, artistCity, artistListener, artistStreams)
                global cityName
                cityName = []
                artistCityArr.append(artistListener)
                cityName.append(artistCity)
    print(cityName, artistCityArr)
    return cityName, artistCityArr
                
fullDate = date.today()
def dayIterator():
    dateList = ['2019-08-15', '2019-09-15', '2019-09-25', '2019-10-01']
    [getMongoData(date) for date in dateList]
    return dateList

def makePlot(cityArr, xArr, yArr):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=xArr, y=yArr, name=cityArr[0], line=dict (color ='blue', width=4)))

    fig.update_layout(title='Shawn Mendes in Jakarta',
                   xaxis_title='Date',
                   yaxis_title='# of Streamers')
    fig.show()

def main():
    getArtistName()
    # dateList = dayIterator()
    # makePlot(cityName, dateList, artistCityArr)

if __name__ == '__main__':
    main()
