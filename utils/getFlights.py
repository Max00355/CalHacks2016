import amadeus
from getKeys import keys


API_KEY = keys['amadeus']['private']

def getCheapestFlights(outOf, to, leaves, returns=None):
    flight = amadeus.Flights(API_KEY)
    return flight.low_fare_search(
        origin=outOf,
        destination=to,
        departure_date=leaves + "" if returns is None else "--{}".format(returns)
    )
