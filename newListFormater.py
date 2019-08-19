import json
import geocoder
import random
import chart_studio.plotly as py
# import plotly.plotly as py #plotly.plotly
import plotly.graph_objs as go
import plotly.figure_factory as FF
import numpy as np
import pandas as pd
import chart_studio
import config
chart_studio.tools.set_credentials_file(username='molyned', api_key='MFfZ6mhOBPu1HNb2af4s')

colourList, cityArray, jsonArray, totalStreams, lonData, latData, data, cityData, streamCount, totalLatData, totalLonData, totalCityData = [], [], [], [], [], [], [], [], [], [], [], []
cityString = ['{"country":"US","region":"IL","city":"Chicago","listeners":1256184},{"country":"US","region":"CA","city":"Los Angeles","listeners":1214212},{"country":"US","region":"NY","city":"New York City","listeners":915071},{"country":"US","region":"TX","city":"Dallas","listeners":891214},{"country":"US","region":"TX","city":"Houston","listeners":743862},{"country":"US","region":"GA","city":"Atlanta","listeners":695900},{"country":"US","region":"NY","city":"Brooklyn","listeners":679001},{"country":"CA","region":"ON","city":"Toronto","listeners":665631},{"country":"MX","region":"CMX","city":"Mexico City","listeners":623572},{"country":"GB","region":"ENG","city":"London","listeners":623030},{"country":"US","region":"CA","city":"San Francisco","listeners":563038},{"country":"BR","region":"SP","city":"S\u00e3o Paulo","listeners":543935},{"country":"US","region":"PA","city":"Philadelphia","listeners":460644},{"country":"FR","region":"75","city":"Paris","listeners":431532},{"country":"NL","region":"NH","city":"Amsterdam","listeners":427937},{"country":"US","region":"FL","city":"Miami","listeners":427822},{"country":"US","region":"OH","city":"Cleveland","listeners":420902},{"country":"CA","region":"QC","city":"Montreal","listeners":415740},{"country":"US","region":"NY","city":"The Bronx","listeners":400797},{"country":"US","region":"WA","city":"Seattle","listeners":399417},{"country":"CL","region":"RM","city":"Santiago","listeners":385868},{"country":"US","region":"NC","city":"Charlotte","listeners":369719},{"country":"US","region":"DC","city":"Washington","listeners":358948},{"country":"US","region":"FL","city":"Orlando","listeners":355593},{"country":"AU","region":"VIC","city":"Melbourne","listeners":351415},{"country":"US","region":"TX","city":"San Antonio","listeners":336500},{"country":"US","region":"CO","city":"Denver","listeners":329684},{"country":"US","region":"VA","city":"Arlington","listeners":323408},{"country":"AU","region":"NSW","city":"Sydney","listeners":323087},{"country":"NO","region":"03","city":"Oslo","listeners":320033},{"country":"US","region":"MN","city":"Minneapolis","listeners":316525},{"country":"US","region":"NV","city":"Las Vegas","listeners":292114},{"country":"US","region":"CA","city":"Anaheim","listeners":279726},{"country":"SE","region":"AB","city":"Stockholm","listeners":279559},{"country":"US","region":"CA","city":"Sacramento","listeners":279190},{"country":"PH","region":"00","city":"Quezon City","listeners":277329},{"country":"IE","region":"L","city":"Dublin","listeners":275867},{"country":"AU","region":"QLD","city":"Brisbane","listeners":262376},{"country":"CA","region":"BC","city":"Vancouver","listeners":259731},{"country":"US","region":"TX","city":"Fort Worth","listeners":256257},{"country":"BR","region":"RJ","city":"Rio de Janeiro","listeners":251148},{"country":"US","region":"AZ","city":"Phoenix","listeners":249380},{"country":"US","region":"CA","city":"San Jose","listeners":242554},{"country":"MX","region":"JAL","city":"Guadalajara","listeners":231648},{"country":"ID","region":"JK","city":"Jakarta","listeners":228678},{"country":"US","region":"MI","city":"Detroit","listeners":227999},{"country":"DE","region":"HE","city":"Frankfurt am Main","listeners":224265},{"country":"US","region":"CA","city":"Oakland","listeners":224147},{"country":"DE","region":"HH","city":"Hamburg","listeners":218215},{"country":"DE","region":"BE","city":"Berlin","listeners":217921}',
'{"country":"ID","region":"JK","city":"Jakarta","listeners":1296070},{"country":"MX","region":"CMX","city":"Mexico City","listeners":1018302},{"country":"PH","region":"00","city":"Quezon City","listeners":965358},{"country":"BR","region":"SP","city":"S\u00e3o Paulo","listeners":936795},{"country":"NL","region":"NH","city":"Amsterdam","listeners":796693},{"country":"US","region":"IL","city":"Chicago","listeners":780847},{"country":"CL","region":"RM","city":"Santiago","listeners":732593},{"country":"US","region":"CA","city":"Los Angeles","listeners":728233},{"country":"US","region":"NY","city":"New York City","listeners":650263},{"country":"ES","region":"M","city":"Madrid","listeners":605546},{"country":"ID","region":"JI","city":"Surabaya","listeners":594768},{"country":"NO","region":"03","city":"Oslo","listeners":593060},{"country":"FR","region":"75","city":"Paris","listeners":567939},{"country":"GB","region":"ENG","city":"London","listeners":553255},{"country":"AR","region":"C","city":"Buenos Aires","listeners":542023},{"country":"SG","region":"","city":"Singapore","listeners":531964},{"country":"US","region":"TX","city":"Dallas","listeners":523303},{"country":"SE","region":"AB","city":"Stockholm","listeners":505149},{"country":"IT","region":"MI","city":"Milan","listeners":493397},{"country":"CA","region":"ON","city":"Toronto","listeners":489377},{"country":"MY","region":"14","city":"Kuala Lumpur","listeners":473269},{"country":"ES","region":"B","city":"Barcelona","listeners":442133},{"country":"TR","region":"34","city":"Istanbul","listeners":419794},{"country":"IT","region":"RM","city":"Rome","listeners":415898},{"country":"US","region":"TX","city":"Houston","listeners":413560},{"country":"MX","region":"JAL","city":"Guadalajara","listeners":409648},{"country":"US","region":"NY","city":"Brooklyn","listeners":400351},{"country":"US","region":"GA","city":"Atlanta","listeners":396990},{"country":"NL","region":"ZH","city":"Rotterdam","listeners":394606},{"country":"BR","region":"RJ","city":"Rio de Janeiro","listeners":394469},{"country":"IE","region":"L","city":"Dublin","listeners":393026},{"country":"CA","region":"QC","city":"Montreal","listeners":390363},{"country":"AU","region":"VIC","city":"Melbourne","listeners":389066},{"country":"US","region":"CA","city":"San Francisco","listeners":384636},{"country":"DE","region":"HH","city":"Hamburg","listeners":380876},{"country":"PH","region":"00","city":"Makati City","listeners":366575},{"country":"DE","region":"HE","city":"Frankfurt am Main","listeners":365867},{"country":"PE","region":"LMA","city":"Lima","listeners":358052},{"country":"AU","region":"NSW","city":"Sydney","listeners":351280},{"country":"DE","region":"BE","city":"Berlin","listeners":340649},{"country":"TH","region":"10","city":"Bangkok","listeners":333551},{"country":"NL","region":"UT","city":"Utrecht","listeners":326091},{"country":"DK","region":"84","city":"Copenhagen","listeners":318110},{"country":"PH","region":"00","city":"San Juan","listeners":302065},{"country":"AU","region":"QLD","city":"Brisbane","listeners":300084},{"country":"PH","region":"00","city":"Manila","listeners":296575},{"country":"DE","region":"BW","city":"Stuttgart","listeners":295452},{"country":"PL","region":"MZ","city":"Warsaw","listeners":292632},{"country":"US","region":"WA","city":"Seattle","listeners":285709},{"country":"DE","region":"BY","city":"Munich","listeners":283351}']
# cleanedString = cityString[cityString.index("[")+1:cityString.index("]")]
for string in cityString:
    cityStringArray = string.split(',{')
    for i in range(len(cityStringArray)):
        if i == 0:
            cityStringArray[i] = cityStringArray[i]
        else:
            cityStringArray[i] = "{" + cityStringArray[i]
        jsonCell = json.loads(cityStringArray[i])
        jsonArray.append(jsonCell)
        streams = 'Monthly Listeners in ' + jsonCell['city'] + ': ' +  str(jsonCell['listeners'])
        
        try:
            streamingLoc = jsonCell['country'] +', ' + jsonCell['city']
            g = geocoder.arcgis(streamingLoc)
            lng = g.json['lng']
            lat = g.json['lat']
        except:
            lng =  'n/a'
            lat =  'n/a'
        streamCount.append(streams)
        cityData.append(streamingLoc)
        latData.append(lat)
        lonData.append(lng)
    totalStreams.append(streamCount[:])
    totalCityData.append(cityData[:])
    totalLatData.append(latData[:])
    totalLonData.append(lonData[:])
    cityData.clear()
    latData.clear()
    lonData.clear()
    streamCount.clear()

# print(totalCityData[1])
# print(totalLatData[1])
# print(totalLonData[1])
# print(totalStreams[1])

# for i in range(len(totalStreams)): 
#     # print(totalStreams[cell])
#     print(totalCityData[i],totalLatData[i], totalLonData[i])

for i in range (2):
    colourOne = random.randint(1,256)
    colourTwo = random.randint(1,256)
    colourThree = random.randint(1,256)
    colour = (colourOne, colourTwo, colourThree)
    goodcolour = str(colour)
    realcolour = 'rgb'+goodcolour
    colourList.append((realcolour))

mapbox_access_token = config.mapAccessToken
for i in range(len(totalCityData)):
    trace = go.Scattermapbox(
            lat=totalLatData[i],
            lon=totalLonData[i],
            name = 'Musician' + str(i),
            mode='markers',
            marker=dict(
                size=10,
                color= colourList[i],
                opacity=0.7
            ),
            text=totalStreams[i],
            
            hoverinfo='text')
    data.append(trace)

# for i in range(len(colourList)):
#     roundNumber = str(i)
#     trace = go.Scattermapbox(
#             lat=latitudeData[i],
#             lon=longitudeData[i],
#             name = str(draftYears[i])+' Class',
#             mode='markers',
#             marker=dict(
#                 size=(i+10)/2,
#                 color= colourList[i],
#                 opacity=0.7
#             ),
#             text=draftClassData[i],
#             hoverinfo='text')
#     #print(latitudeData[i])
#     data.append(trace)

layout = go.Layout(
    title='Drake and Shawn Music Test',
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
    # legend =  True #dict(
    #     #    traceorder = 'reversed'
    # # )

)

fig = dict(data=data, layout=layout)
py.plot(fig, filename='Drake and Shawn Music Test V1')