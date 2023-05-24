from tire import Tire


class CarriganTire(Tire):
    def __init__(self, tire_array):
        self.tire_array = tire_array

    def needs_service(self):
        for num in self.tire_array:
            if num >= 0.9:
                return True
        return False
