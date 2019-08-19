import json
from geopy.geocoders import Nominatim
# import geocoder
cityString = '":[{"country":"US","region":"IL","city":"Chicago","listeners":1256184},{"country":"US","region":"CA","city":"Los Angeles","listeners":1214212},{"country":"US","region":"NY","city":"New York City","listeners":915071},{"country":"US","region":"TX","city":"Dallas","listeners":891214},{"country":"US","region":"TX","city":"Houston","listeners":743862},{"country":"US","region":"GA","city":"Atlanta","listeners":695900},{"country":"US","region":"NY","city":"Brooklyn","listeners":679001},{"country":"CA","region":"ON","city":"Toronto","listeners":665631},{"country":"MX","region":"CMX","city":"Mexico City","listeners":623572},{"country":"GB","region":"ENG","city":"London","listeners":623030},{"country":"US","region":"CA","city":"San Francisco","listeners":563038},{"country":"BR","region":"SP","city":"S\u00e3o Paulo","listeners":543935},{"country":"US","region":"PA","city":"Philadelphia","listeners":460644},{"country":"FR","region":"75","city":"Paris","listeners":431532},{"country":"NL","region":"NH","city":"Amsterdam","listeners":427937},{"country":"US","region":"FL","city":"Miami","listeners":427822},{"country":"US","region":"OH","city":"Cleveland","listeners":420902},{"country":"CA","region":"QC","city":"Montreal","listeners":415740},{"country":"US","region":"NY","city":"The Bronx","listeners":400797},{"country":"US","region":"WA","city":"Seattle","listeners":399417},{"country":"CL","region":"RM","city":"Santiago","listeners":385868},{"country":"US","region":"NC","city":"Charlotte","listeners":369719},{"country":"US","region":"DC","city":"Washington","listeners":358948},{"country":"US","region":"FL","city":"Orlando","listeners":355593},{"country":"AU","region":"VIC","city":"Melbourne","listeners":351415},{"country":"US","region":"TX","city":"San Antonio","listeners":336500},{"country":"US","region":"CO","city":"Denver","listeners":329684},{"country":"US","region":"VA","city":"Arlington","listeners":323408},{"country":"AU","region":"NSW","city":"Sydney","listeners":323087},{"country":"NO","region":"03","city":"Oslo","listeners":320033},{"country":"US","region":"MN","city":"Minneapolis","listeners":316525},{"country":"US","region":"NV","city":"Las Vegas","listeners":292114},{"country":"US","region":"CA","city":"Anaheim","listeners":279726},{"country":"SE","region":"AB","city":"Stockholm","listeners":279559},{"country":"US","region":"CA","city":"Sacramento","listeners":279190},{"country":"PH","region":"00","city":"Quezon City","listeners":277329},{"country":"IE","region":"L","city":"Dublin","listeners":275867},{"country":"AU","region":"QLD","city":"Brisbane","listeners":262376},{"country":"CA","region":"BC","city":"Vancouver","listeners":259731},{"country":"US","region":"TX","city":"Fort Worth","listeners":256257},{"country":"BR","region":"RJ","city":"Rio de Janeiro","listeners":251148},{"country":"US","region":"AZ","city":"Phoenix","listeners":249380},{"country":"US","region":"CA","city":"San Jose","listeners":242554},{"country":"MX","region":"JAL","city":"Guadalajara","listeners":231648},{"country":"ID","region":"JK","city":"Jakarta","listeners":228678},{"country":"US","region":"MI","city":"Detroit","listeners":227999},{"country":"DE","region":"HE","city":"Frankfurt am Main","listeners":224265},{"country":"US","region":"CA","city":"Oakland","listeners":224147},{"country":"DE","region":"HH","city":"Hamburg","listeners":218215},{"country":"DE","region":"BE","city":"Berlin","listeners":217921}]}}</script>'
cleanedString = cityString[cityString.index("[")+1:cityString.index("]")]
cityArray = cleanedString.split(',{')
jsonArray, objArray, lonData, latData = [], [], [], []

# urlList = ['https://open.spotify.com/artist/7n2wHs1TKAczGzO7Dd2rGr/about',
#             'https://open.spotify.com/artist/4nDoRrQiYLoBzwC5BhVJzF/about',
#             'https://open.spotify.com/artist/246dkjvS1zLTtiykXe5h60/about',
#             'https://open.spotify.com/artist/06HL4z0CvFAxyc27GXpf02/about',
#             'https://open.spotify.com/artist/1sBkRIssrMs1AbVkOJbc7a/about',
#             'https://open.spotify.com/artist/66CXWjxzNUsdJxJ2JdwvnR/about',
#             'https://open.spotify.com/artist/6eUKZXaKkcviH0Ku9w2n3V/about',
#             'https://open.spotify.com/artist/6LuN9FCkKOj5PcnpouEgny/about',
#             'https://open.spotify.com/artist/1uNFoZAHBGtllmzznpCI3s/about',
#             'https://open.spotify.com/artist/7jVv8c5Fj3E9VhNjxT4snq/about',
#             'https://open.spotify.com/artist/60rpJ9SgigSd16DOAG7GSa/about',
#             'https://open.spotify.com/artist/7bXgB6jMjp9ATFy66eO08Z/about',
#             'https://open.spotify.com/artist/6l3HvQ5sa6mXTsMTB19rO5/about',
#             'https://open.spotify.com/artist/0Y5tJX1MQlPlqiwlOH1tJY/about',
#             'https://open.spotify.com/artist/69GGBxA162lTqCwzJG5jLp/about',
#             'https://open.spotify.com/artist/6qqNVTkY8uBg9cP3Jd7DAH/about',
#             'https://open.spotify.com/artist/2wY79sveU1sp5g7SokKOiI/about',
#             'https://open.spotify.com/artist/0hCNtLu0JehylgoiP8L4Gh/about',
#             'https://open.spotify.com/artist/3JhNCzhSMTxs9WLGJJxWOY/about',
#             'https://open.spotify.com/artist/23fqKkggKUBHNkbKtXEls4/about',
#             'https://open.spotify.com/artist/0du5cEVh5yTK9QJze8zA0C/about',
#             'https://open.spotify.com/artist/04gDigrS5kc9YWfZHwBETP/about',
#             'https://open.spotify.com/artist/5pKCCKE2ajJHZ9KAiaK11H/about',
#             'https://open.spotify.com/artist/4VMYDCV2IEDYJArk749S6m/about',
#             'https://open.spotify.com/artist/4gzpq5DPGxSnKTe4SA8HAU/about',
#             'https://open.spotify.com/artist/6deZN1bslXzeGvOLaLMOIF/about',
#             'https://open.spotify.com/artist/4dpARuHxo51G3z768sgnrY/about',
#             'https://open.spotify.com/artist/1Xyo4u8uXC1ZmMpatF05PJ/about',
#             'https://open.spotify.com/artist/3gd8FJtBJtkRxdfbTu19U2/about',
#             'https://open.spotify.com/artist/20sxb77xiYeusSH8cVdatc/about',
#             'https://open.spotify.com/artist/55Aa2cqylxrFIXC767Z865/about',
#             'https://open.spotify.com/artist/17lzZA2AlOHwCwFALHttmp/about',
#             'https://open.spotify.com/artist/0YMeriqrS3zgsX24nfY0F0/about',
#             'https://open.spotify.com/artist/2YZyLoL8N0Wb9xBt1NhZWg/about',
#             'https://open.spotify.com/artist/4V8LLVI7PbaPR0K2TGSxFF/about',
#             'https://open.spotify.com/artist/0LcJLqbBmaGUft1e9Mm8HV/about',
#             'https://open.spotify.com/artist/5K4W6rqBFWDnAN6FQUkS6x/about',
#             'https://open.spotify.com/artist/3jK9MiCrA42lLAdMGUZpwa/about',
#             'https://open.spotify.com/artist/08yf5A2nS4XEeNvabDXqyg/about',
#             'https://open.spotify.com/artist/4UXqAaa6dQYAk18Lv7PEgX/about',
#             'https://open.spotify.com/artist/7dGJo4pcD2V6oG8kP0tJRR/about',
#             'https://open.spotify.com/artist/2o5jDhtHVPhrJdv3cEQ99Z/about',
#             'https://open.spotify.com/artist/1vyhD5VmyZ7KMfW5gqLgo5/about',
#             'https://open.spotify.com/artist/540vIaP2JwjQb9dm3aArA4/about',
#             'https://open.spotify.com/artist/0EmeFodog0BfCgMzAIvKQp/about',
#             'https://open.spotify.com/artist/1vCWHaC5f2uS3yhpwWbIA6/about',
#             'https://open.spotify.com/artist/77AiFEVeAVj2ORpC85QVJs/about',
#             'https://open.spotify.com/artist/6cEuCEZu7PAE9ZSzLLc2oQ/about',
#             'https://open.spotify.com/artist/2XnBwblw31dfGnspMIwgWz/about',
#             'https://open.spotify.com/artist/1Cs0zKBU1kc0i8ypK3B9ai/about',
#             'https://open.spotify.com/artist/64KEffDW9EtZ1y2vBYgq8T/about',
#             'https://open.spotify.com/artist/0C0XlULifJtAgn6ZNCW2eu/about',
#             'https://open.spotify.com/artist/7jy3rLJdDQY21OgRLCZ9sD/about',
#             'https://open.spotify.com/artist/1dfeR4HaWDbWqFHLkxsg1d/about',
#             'https://open.spotify.com/artist/3WrFJ7ztbogyGnTHbHJFl2/about',]

for i in range(len(cityArray)):
    
    if i == 0:
        cityArray[i] = cityArray[i]
    else:
        cityArray[i] = "{" + cityArray[i]
    jsonArray.append(cityArray[i])
for dataCell in jsonArray:
    jsonCell = json.loads(dataCell)
    objArray.append(jsonCell)

for x in objArray:
    # print(x['country'] +', ' + x['region'] +', ' + x['city'], x['listeners'])
    try:
        streamingLoc = x['country'] +', ' + x['region'] +', ' + x['city']
        geolocator = Nominatim()
        # loc = geolocator.geocode(streamingLoc)
        # lon = (loc.longitude)
        # loc = geolocator.geocode(streamingLoc)
        # lat = (loc.latitude)
        g = geocoder.google(streamingLoc)
        g.latlng
        # print(streamingLoc, lat, lon)
    except:
        lon =  'n/a'
        lat =  'n/a'
        print(streamingLoc, lat, lon)
    latData.append((lat))
    lonData.append((lon))

