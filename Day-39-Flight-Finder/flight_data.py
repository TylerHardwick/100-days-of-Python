class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self, price, flyfrom, cityfrom, flyto, cityto, out_date, return_date ):
        self.price = price
        self.departure_airport_code = flyfrom
        self.departure_city = cityfrom
        self.arriving_airport_code = flyto
        self.arriving_city = cityto
        self.out_date = out_date
        self.return_date = return_date
