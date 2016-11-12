import sendText
import getFlights
import pprint

def smartResponse(to, inputText):

    # Send initial text
    sendText.sendText(to, "Here are some flights we found...")

    # Turn input text into "outOf, to, leaves" -> NOT DOING THIS YET

    # Determine what kind of request it is, cheap / first class / etc. -> RIGHT NOW ONLY DOING CHEAPEST
    outputText = cheapestFlightResponse(inputText)

    # send text message
	sendText.sendText(to, outputText)

def cheapestFlightResponse(inputText):

    outOf, to, leaves = inputText.strip().split(' ')
    flightJson = getCheapestFlights(outOf, to, leaves)

    result = flightJson["results"][0]

    refundable = result["fare"]["restrictions"]["refundable"]
    fare = result["fare"]["total_price"]

    flight0 = result["itineraries"][0]["outbound"]["flights"]

    airline = flight0["operating_airline"]
    flightNumber = flight0["flight_number"]

    departsAt = flight0["departs_at"]
    originAirport = flight0["origin"]["airport"]
    originTerminal = flight0["origin"]["terminal"]

    arrivesAt = flight0["arrives_at"]
    destinationAirport = flight0["destination"]["airport"]
    destinationTerminal = flight0["destination"]["terminal"]

    outputText = "There is a $" + fare + " " + airline + " flight that departs from " + originAirport + ", terminal " + originTerminal + " at " + departs_at + " and arrives at " + destinationAirport + ", terminal " + destinationTerminal + " at " + arrives_at + ". Flight number " + flight_number

    return outputText



