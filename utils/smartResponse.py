import getAirline
import sendText
import getFlights
import getHotels
import getCarRentals
import toDate
import pprint
from flask import session
import getAirportCode
from db import db
import pprint
import json
import convertDate

def smartResponse(messageType, variables): # Will change to smartResponse(to, messageType, variables)

    # Turn input text into "outOf, to, leaves" -> NOT DOING THIS YET

    # Determine what kind of request it is, cheap / first class / etc. -> RIGHT NOW ONLY DOING CHEAPEST

    if messageType == "getFlights":
        outputList = cheapestFlightResponse(variables)
        if len(outputList) == 0:
            outputList = ["Sorry, we weren't able to find anything for you!"]
        elif len(outputList) < 3:
            outputList = outputList
        else:
            outputList = outputList[:3]
    elif messageType == "getHotels":
        outputList = cheapestHotelsResponse(variables)[:2]
    elif messageType == "getCarRentals":
        outputList = cheapestCarRentalsResponse(variables)[:2]
    else:
        outputList = ["Sorry, I'm not sure I understand."] 
    # Send output texts
    return '\n--\n'.join(outputList)

def codeToFullName(originAirport):
    return originAirport
    airportsJsonData = json.load(open("utils/airportsJson.json"))

    for state in airportsJsonData: # Turn origin airport into real name rather than code
	for airportKey, airportValue in airportsJsonData[state].items():
	    if airportValue == originAirport:
		originAirport = airportKey + "(" + airportValue + ")"
                return originAirport
    return originAirport
    

def cheapestFlightResponse(variables):

    outOf = variables['from']
    to = variables['to']
    leaves = convertDate.convertDate(variables['date'])
    outOf = getAirportCode.getAirportCode(outOf)
    to = getAirportCode.getAirportCode(to)

    flightJson = getFlights.getCheapestFlights(outOf, to, leaves)
    if "message" in flightJson.keys():
        return [flightJson['message']]


    outputList = []
    flightNumber_ = 1    
    for result in flightJson.get("results", [])[:3]:
        price = result.get("fare", {}).get("total_price", "Unknown")
        for flights in result.get("itineraries", []):
            connecting = flights.get("outbound", {}).get("flights", [])
            isConnecting = "Connecting Flight" if len(connecting) > 1 else "Non Stop"
            builtFlight = "Flight Number: {}\nPrice: {}\n{}\n".format(flightNumber_, price, isConnecting)
            for flight in connecting:
                aircraftType  = flight.get("aircraft", "Unknown")
                leaves_at = toDate.toDate(flight.get("departs_at", "Unknown"))
                seatsRemaining = flight.get("booking_info", {}).get("seats_remaining", "Unknown")
                travel_class = flight.get("booking_info", {}).get("travel_class", "Unknown")
                destination = codeToFullName(flight.get("destination", {}).get("airport", "Unknown"))
                flightNumber = flight.get("flight_number", "Unknown")
                airline = flight.get("operating_airline", "Unknown")
                origin = codeToFullName(flight.get("origin", {}).get("airport", "Unknown"))
                terminal = flight.get("origin", {}).get("terminal", "Unknown")
                flightInfo = """
Aircraft: {}
Departing at: {}
Seats Remaining: {}
Class: {}
Origin: {}
Destinaton: {}
Flight Number: {}
Airline: {}
Terminal: {}

                """.format(aircraftType, leaves_at, seatsRemaining, travel_class, origin, destination, flightNumber, airline, terminal)
                builtFlight += flightInfo
            outputList.append(builtFlight)
        flightNumber_ += 1
    return outputList

def cheapestHotelsResponse(variables):
    location = variables['location']
    radius = variables['radius']
    checkIn = variables['checkIn']
    checkOut = variables['checkOut']

    hotelsJson = getHotels.getCheapestHotels(location, radius, checkIn, checkOut)
    if "message" in hotelsJson.keys():
        return [hotelsJson['message']]

    outputList = []
    for result in hotelsJson["results"]:
        propertyName = result["property_name"]
        totalPrice = result["total_price"]["amount"]
        phone = "Unknown"
        for i in result["contacts"]:
            if i["type"] == "PHONE":
                phone = i["detail"]
                break
        address = result["address"].get("line1", "") + ", " + result["address"].get("city", "") + ", " + result["address"].get("region", "") + " " + str(result["address"].get("postal_code", ""))

        outputText = ""
        outputText += propertyName + "\n\n"
        outputText += "Address: " + address + "\n\n"
        outputText += "Total cost: " + str(totalPrice) + "\n\n"
        outputText += "Phone #: " + str(phone)

        outputList.append(outputText)

    return outputList

def cheapestCarRentalsResponse(variables):
    location = variables['location']
    radius = variables['radius']
    pickUp = variables['pickUp']
    dropOff = variables['dropOff']

    carsJson = getCarRentals.getCheapestCarRentals(location, radius, pickUp, dropOff)
    if "message" in carsJson.keys():
        return [hotelsJson['message']]

    outputList = []
    for result in carsJson["results"]:
        provider = result["provider"]["company_name"]
        address = result["address"].get("line1", "") + ", " + result["address"].get("city", "") + ", " + result["address"].get("region", "") + " " + str(result["address"].get("postal_code", ""))
        numberOfCars = str(len(result["cars"]))

        outputText = ""
        outputText += "Provider: " + provider + "\n\n"
        outputText += "Address: " + address + "\n\n"
        outputText += "Total cars: " + numberOfCars

        outputList.append(outputText)

    return outputList






