# 2. Create a child class Bus
# that will inherit all of the variables and methods of the Vehicle class
# and will have seating_capacity own method
from vehicle import Vehicle

class Bus(Vehicle):
    def __init__(self, max_speed, mileage, seating_capacity):
        super().__init__(max_speed, mileage)
        self.seating_capacity = seating_capacity

    def get_seating_capacity(self):
        print(f"This bus's seating_capacity is {self.seating_capacity()}")