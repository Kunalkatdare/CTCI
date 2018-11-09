class ParkingLot(object):
    def __init__(self):
        self.cars = {}

    def park_car(self, car):
        self.cars[car] = True

    def unpark_car(self, car):
        self.cars[car] = False


class Car(object):
    pass


class Solution(object):
    def test(self):
        lot = ParkingLot()
        car1 = Car()
        car2 = Car()
        lot.park_car(car1)
        lot.park_car(car2)
        lot.unpark_car(car1)
