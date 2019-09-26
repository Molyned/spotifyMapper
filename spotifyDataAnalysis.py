import pymongo
import json
import config
import pandas as pd
from datetime import date, timedelta

client = pymongo.MongoClient('mongodb+srv://molyned:{}@spotifycluster-6btnk.mongodb.net/test?retryWrites=true&w=majority'.format(config.MONGO_PASSWORD))
database = client.business

collection2 = database.artistInfo2
collection3 = database.artistInfo2['2019-09-25']

myCursor2 = collection2.find()
myCursor3 = collection3.find()

def topArtistPerCity():
    totalDf = pd.DataFrame(columns=['Artist Name', 'Max Listeners', 'Location'])
    maxCityDf = pd.DataFrame(columns=['Artist Name', 'Max Listeners', 'Location'])
    for item in myCursor2:
        artistName = item['name']
        artistArray = item['artist']['cities']
        for row in artistArray:
            artistListener =  row['listeners']
            
            artistCity =  row['city']
            totalDf.loc[len(totalDf)] = [artistName, artistListener, artistCity]

    totalDf = totalDf.sort_values(['Location', 'Max Listeners'], ascending=False).reset_index()
    print(totalDf)
    for row in totalDf.itertuples(index=True):
        print(totalDf.iloc[row.Index])
        print(totalDf.iloc[row.Index+1])
        # streamers = row[2]
        # city = row[4]
        # nextCity = row[4].Index+1
        # if city != nextCity:
        #     print(city, nextCity)

    #     # totalDf.at[row.Index, 'Annotation transcript'] = cell1


def totalTopArtists():
    maxList1 = pd.DataFrame(columns=['Artist Name', 'Max Listeners', 'Location'])
    maxList2 = pd.DataFrame(columns=['Artist Name', 'Max Listeners', 'Location'])
    for item in myCursor2:
        artistListeners = item['artist']['cities'][0]['listeners'] 
        artistCity = item['artist']['cities'][0]['city'] 
        artistName = item['name']
        maxList1.loc[len(maxList1)] = [artistName, artistListeners, artistCity]

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