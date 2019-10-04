import pymongo
import json
import config
import pandas as pd
from datetime import date, timedelta

import pandas as pd
import numpy as np
import matplotlib
import cufflinks as cf
import plotly
import plotly.offline as py
import plotly.graph_objs as go

cf.go_offline()

client = pymongo.MongoClient('mongodb+srv://molyned:{}@spotifycluster-6btnk.mongodb.net/test?retryWrites=true&w=majority'.format(config.MONGO_PASSWORD))
database = client.business

collection2 = database.artistInfo2
collection3 = database.artistInfo2['2019-09-25']

myCursor3 = collection3.find()

def topArtistPerCity():
    totalDf = pd.DataFrame(columns=['Artist Name', 'Max Listeners', 'Location'])
    maxCityDf = pd.DataFrame(columns=['Artist Name', 'Max Listeners', 'Location'])
    for item in myCursor3:
        artistName = item['name']
        artistArray = item['artist']['cities']
        for row in artistArray:
            artistListener =  row['listeners']
            
            artistCity =  row['city']
            totalDf.loc[len(totalDf)] = [artistName, artistListener, artistCity]

    totalDf = totalDf.sort_values(['Location', 'Max Listeners'], ascending=False) #.reset_index()

    # print(totalDf)
    totalDf = totalDf.groupby(['Location']).max().reset_index() #.mean()
    # print(totalDf)
    # for row in totalDf.itertuples(index=True):
    #     print(row)
    # count = 0 
    # startingRowIndex = 0 
    # testCount = 0
    # for row in totalDf.itertuples(index=True):
    #     firstRowCity = totalDf.iloc[row.Index, 3]
    #     try:
    #         nextRowCity = totalDf.iloc[row.Index+1, 3]
    #     except:
    #         break
    #     if firstRowCity == nextRowCity:
    #         count = count + 1
    #     elif (firstRowCity != nextRowCity) and (count == 0):
    #         print('Done in ELIF statement', firstRowCity, nextRowCity)
    #         count = 1
    #         endingIndex = startingRowIndex + count
    #         print(startingRowIndex, endingIndex, count)
    #         print(totalDf.iloc[startingRowIndex:endingIndex, 1:4])
    #         startingRowIndex = startingRowIndex + count + 1
    #         count = 0
    #         print(startingRowIndex)
    #         print('---------------------------------------------')
    #     else: 
    #         print('Done in ELSE statement', firstRowCity, nextRowCity)
    #         endingIndex = startingRowIndex + count
    #         print(startingRowIndex, endingIndex, count)
    #         print(totalDf.iloc[startingRowIndex:endingIndex, 1:4])
    #         startingRowIndex = startingRowIndex + count + 1
    #         count = 0
    #         print(startingRowIndex)
    #         print('---------------------------------------------')
    #     testCount =  testCount +1            

def totalTopArtists():
    maxList1 = pd.DataFrame(columns=['Artist Name', 'Max Listeners', 'Location'])
    maxList2 = pd.DataFrame(columns=['Artist Name', 'Max Listeners', 'Location'])
    # for item in myCursor2:
    #     artistListeners = item['artist']['cities'][0]['listeners'] 
    #     artistCity = item['artist']['cities'][0]['city'] 
    #     artistName = item['name']
    #     maxList1.loc[len(maxList1)] = [artistName, artistListeners, artistCity]

    for item in myCursor3:
        artistListeners = item['artist']['cities'][0]['listeners'] 
        artistCity = item['artist']['cities'][0]['city'] 
        artistName = item['name']
        maxList2.loc[len(maxList2)] = [artistName, artistListeners, artistCity]

    maxList1 = maxList1.sort_values(by ='Max Listeners', ascending=False).reset_index()
    maxList2 = maxList2.sort_values(by ='Max Listeners', ascending=False).reset_index()
    print(maxList1.head())
    print(maxList2.head())

def main():
    topArtistPerCity()
    # totalTopArtists()
if __name__ == '__main__':
    main()