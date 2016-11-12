import json

def getAirline(code):
    return json.load(open("utils/airline.json")).get(code, code)
