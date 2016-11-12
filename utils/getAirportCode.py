import json

def getAirportCode(airportName, state=None):
    if len(airportName) == 3:
        citiesAbbr = json.load(open("utils/citiesAbbrJson.json"))
        if airportName in citiesAbbr.keys():
            airportName = citiesAbbr[airportName]
        else:
            return airportName
    jsonData = json.load(open("utils/airportsJson.json"))
    bestMatch = {
        "bestMatch":-1,
        "airport":None
    }
    if jsonData.get(airportName.lower()):
        state = airportName.lower()
    if state:
        jsonData = jsonData[state.lower()]
        for name in jsonData:
            nameLower = name.lower()
            matchValue = 0
            for text in airportName.split():
                text = text.lower()
                if text in nameLower:
                    matchValue += 1
            if matchValue > bestMatch['bestMatch']:
                bestMatch['bestMatch'] = matchValue
                bestMatch['airport'] = jsonData[name]
    else:
        for state in jsonData:
            for name in jsonData[state]:
                nameLower = name.lower()
                matchValue = 0
                for text in airportName.split():
                    text = text.lower()
                    if text in nameLower:
                        matchValue += 1
                if matchValue > bestMatch['bestMatch']:
                    bestMatch['bestMatch'] = matchValue
                    bestMatch['airport'] = jsonData[state][name]
           
    return bestMatch['airport']


