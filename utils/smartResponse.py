import sendText
import getFlights
import toDate
import pprint

def smartResponse(to, inputText):

    # Send initial text
    sendText.sendText(to, "Here are some flights we found...")

    # Turn input text into "outOf, to, leaves" -> NOT DOING THIS YET

    # Determine what kind of request it is, cheap / first class / etc. -> RIGHT NOW ONLY DOING CHEAPEST
    outputList = cheapestFlightResponse(inputText)

    # Send output texts
    for outputText in outputList:
        sendText.sendText(to, outputText)

def cheapestFlightResponse(inputText):

    outOf, to, leaves = inputText.strip().split(' ')
    flightJson = getFlights.getCheapestFlights(outOf, to, leaves)
    if "message" in flightJson.keys():
        return flightJson['message']
    result = flightJson["results"][0]

    refundable = result["fare"]["restrictions"]["refundable"]
    fare = result["fare"]["total_price"]
    flights = result["itineraries"][0]["outbound"]["flights"]
    outputList = []
    for flight in flights:
        airline = flight["operating_airline"]
        flightNumber = flight["flight_number"]

        departsAt = toDate.toDate(flight["departs_at"])
        originAirport = flight["origin"]["airport"]
        originTerminal = flight["origin"]["terminal"]
        
        arrivesAt = toDate.toDate(flight["arrives_at"])
        destinationAirport = flight["destination"]["airport"]
        destinationTerminal = flight["destination"]["terminal"]

        outputText = ""
        outputText += "$" + fare + " " + airline + " flight" + "\n\n"
        outputText += "Departs from " + originAirport + ", terminal " + originTerminal + " on " + departsAt + "\n\n"
        outputText += "Arrives at " + destinationAirport + ", terminal " + destinationTerminal + " on " + arrivesAt + "\n\n"
        outputText += "Flight number: " + flightNumber

        outputList.append(outputText)
    return outputList



