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
        outputList = cheapestFlightResponse(variables)[:3]
    elif messageType == "getHotels":
        outputList = cheapestHotelsResponse(variables)[:2]
    elif messageType == "getCarRentals":
        outputList = cheapestCarRentalsResponse(variables)[:2]
    else:
        outputList = ["Sorry, I'm not sure I understand."] 
    # Send output texts
    return '\n\n----------\n\n'.join(outputList)

def cheapestFlightResponse(variables):

    outOf = variables['from']
    to = variables['to']
    leaves = convertDate.convertDate(variables['date'])

    outOf = getAirportCode.getAirportCode(outOf)
    to = getAirportCode.getAirportCode(to)

    flightJson = getFlights.getCheapestFlights(outOf, to, leaves)
    if "message" in flightJson.keys():
        return [flightJson['message']]

    airportsJsonData = json.load(open("utils/airportsJson.json"))

    outputList = []
    for result in flightJson["results"]:
        refundable = result["fare"]["restrictions"].get("refundable", "False")
        fare = result.get("fare", {}).get("total_price", "Unknown")

        itinerary_list = []
        for itinerary in result.get("itineraries", []):
            flight = itinerary.get("outbound", {}).get("flights")[0]
            #for flight in flights:
            airline = getAirline.getAirline(flight.get("operating_airline", "Unknown"))
            flightNumber = flight.get("flight_number", "Unknown")

            departsAt = toDate.toDate(flight.get("departs_at", "Unknown"))
            originAirport = flight.get("origin", {}).get("airport", "Unknown")
            originTerminal = flight.get("origin", {}).get("terminal", "Unknown")
            
            if flight.get("arrives_at"):
                arrivesAt = toDate.toDate(flight["arrives_at"])
            else:
                arrivesAt = "Unknown"
            destinationAirport = flight.get("destination", {}).get("airport", "Unknown")
            destinationTerminal = flight.get("destination", "Unknown").get("terminal", "Unknown")

            # Check if matching, proper flights!!
            if originAirport == outOf and destinationAirport == to:
                print("MATCHED")

                # Fix so displays corrent values
                for state in airportsJsonData: # Turn origin airport into real name rather than code
                    for airportKey, airportValue in airportsJsonData[state].items():
                        if airportValue == originAirport:
                            originAirport = airportKey + "(" + airportValue + ")"

                for state in airportsJsonData: # Turn destinationAirport airport into real name rather than code
                    for airportKey, airportValue in airportsJsonData[state].items():
                        if airportValue == destinationAirport:
                            destinationAirport = airportKey + "(" + airportValue + ")"

                # Since matched, create text
                itineraryText = ""
                itineraryText += "$" + fare + " " + airline + " flight" + "\n\n"
                itineraryText += "Departs from " + originAirport + ", terminal " + originTerminal + " on " + departsAt + "\n\n"
                itineraryText += "Arrives at " + destinationAirport + ", terminal " + destinationTerminal + " on " + arrivesAt + "\n\n"
                itineraryText += "Flight number: " + flightNumber

                # Append to list
                outputList.append(itineraryText)

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






