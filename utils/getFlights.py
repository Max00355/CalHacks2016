import amadeus

API_KEY = "ikjnlVEIoDIonA0RaGak9TGmgTKGhhcv"

def getCheapestFlights(outOf, to, leaves, returns=None):
    flight = amadeus.Flights(API_KEY)
    return flight.low_fare_search(
        origin=outOf,
        destination=to,
        departure_date=leaves + "" if returns is None else "--{}".format(returns)
    )
    
