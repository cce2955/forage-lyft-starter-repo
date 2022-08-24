class engine:
    def __init__(self, last_service_mileage:int, currentMileage:int):
        self.last_service_milage:int
        self.currentMilage:int

    def needs_Service(self, minMileage:int):
        return self.current_mileage - self.last_service_mileage > minMileage