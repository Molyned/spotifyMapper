import json
cityString = ('":[{"country":"US","region":"IL","city":"Chicago","listeners":1256184},'
'{"country":"US","region":"CA","city":"Los Angeles","listeners":1214212},'
'{"country":"US","region":"NY","city":"New York City","listeners":915071},'
'{"country":"US","region":"TX","city":"Dallas","listeners":891214},'
'{"country":"US","region":"TX","city":"Houston","listeners":743862},'
'{"country":"US","region":"GA","city":"Atlanta","listeners":695900},'
'{"country":"US","region":"NY","city":"Brooklyn","listeners":679001},'
'{"country":"CA","region":"ON","city":"Toronto","listeners":665631},'
'{"country":"MX","region":"CMX","city":"Mexico City","listeners":623572},'
'{"country":"GB","region":"ENG","city":"London","listeners":623030},{"country":"US","region":"CA","city":"San Francisco","listeners":563038},'
'{"country":"BR","region":"SP","city":"S\u00e3o Paulo","listeners":543935},{"country":"US","region":"PA","city":"Philadelphia","listeners":460644},'
'{"country":"FR","region":"75","city":"Paris","listeners":431532},{"country":"NL","region":"NH","city":"Amsterdam","listeners":427937},'
'{"country":"US","region":"FL","city":"Miami","listeners":427822},{"country":"US","region":"OH","city":"Cleveland","listeners":420902},'
'{"country":"CA","region":"QC","city":"Montreal","listeners":415740},{"country":"US","region":"NY","city":"The Bronx","listeners":400797},'
'{"country":"US","region":"WA","city":"Seattle","listeners":399417},{"country":"CL","region":"RM","city":"Santiago","listeners":385868},'
'{"country":"US","region":"NC","city":"Charlotte","listeners":369719},{"country":"US","region":"DC","city":"Washington","listeners":358948},'
'{"country":"US","region":"FL","city":"Orlando","listeners":355593},{"country":"AU","region":"VIC","city":"Melbourne","listeners":351415},'
'{"country":"US","region":"TX","city":"San Antonio","listeners":336500},{"country":"US","region":"CO","city":"Denver","listeners":329684},'
'{"country":"US","region":"VA","city":"Arlington","listeners":323408},{"country":"AU","region":"NSW","city":"Sydney","listeners":323087},'
'{"country":"NO","region":"03","city":"Oslo","listeners":320033},{"country":"US","region":"MN","city":"Minneapolis","listeners":316525},'
'{"country":"US","region":"NV","city":"Las Vegas","listeners":292114},{"country":"US","region":"CA","city":"Anaheim","listeners":279726},'
'{"country":"SE","region":"AB","city":"Stockholm","listeners":279559},{"country":"US","region":"CA","city":"Sacramento","listeners":279190},'
'{"country":"PH","region":"00","city":"Quezon City","listeners":277329},{"country":"IE","region":"L","city":"Dublin","listeners":275867},'
'{"country":"AU","region":"QLD","city":"Brisbane","listeners":262376},{"country":"CA","region":"BC","city":"Vancouver","listeners":259731},'
'{"country":"US","region":"TX","city":"Fort Worth","listeners":256257},{"country":"BR","region":"RJ","city":"Rio de Janeiro","listeners":251148},'
'{"country":"US","region":"AZ","city":"Phoenix","listeners":249380},{"country":"US","region":"CA","city":"San Jose","listeners":242554},'
'{"country":"MX","region":"JAL","city":"Guadalajara","listeners":231648},{"country":"ID","region":"JK","city":"Jakarta","listeners":228678},'
'{"country":"US","region":"MI","city":"Detroit","listeners":227999},{"country":"DE","region":"HE","city":"Frankfurt am Main","listeners":224265},'
'{"country":"US","region":"CA","city":"Oakland","listeners":224147},{"country":"DE","region":"HH","city":"Hamburg","listeners":218215},'
'{"country":"DE","region":"BE","city":"Berlin","listeners":217921}]}};</script>')
cleanedCity = cityString[cityString.find("[")+1:cityString.find("]")]

cityArray = [] #eval('{"country":"US","region":"CA","city":"Los Angeles","listeners":1214212}')
splitString = cleanedCity.split(',{')
for i in range(len(splitString)):
    # print(splitString[i])
    if i == 0: 
        properNames = splitString[i]
    else:
        properNames = '{' + splitString[i]
    cityArray.append(properNames)
# print(cityArray)

for i in range(len(cityArray)):
    cityObj = json.loads(cityArray[i])
    print(cityObj['country'], cityObj['city'], cityObj['listeners'])

