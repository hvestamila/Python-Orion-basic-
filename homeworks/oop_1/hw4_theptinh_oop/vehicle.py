# 1. Create a Vehicle class with max_speed and mileage instance attributes
class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

    def get_info(self):
        print(f'This vehicle max speed is {self.max_speed} and miliage is {self.mileage}')
