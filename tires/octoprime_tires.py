
class octoPrimeTires(Tires):
    def __init__(self, driverFront, driverBack, passengerFront, passengerBack):
        self.driverFront = driverFront
        self.driverBack = driverBack
        self.passengerFront = passengerFront
        self.passengerBack = passengerBack

    def needs_service(self):
        sum = self.driverBack + self.driverFront + self.passengerBack + self.passengerFront
        if sum > 3:
            return True
        else:
            return False