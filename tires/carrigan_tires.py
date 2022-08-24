
from tires.tires import Tires


class carriganTires(Tires):
    def __init__(self, driverFront, driverBack, passengerFront, passengerBack):
        self.driverFront = driverFront
        self.driverBack = driverBack
        self.passengerFront = passengerFront
        self.passengerBack = passengerBack

    def needs_service(self):
        if self.driverFront > 0.9 or self.driverBack > 0.9 or self.passengerFront > 0.9 or self.passengerBack > 0.9:
            return True
        else:
            return False