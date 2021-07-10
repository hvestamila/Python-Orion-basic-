# 6*. Create a new class SchoolBus that will inherit all of the methods from School and Bus
# and will have its own - bus_school_color
from school import School
from bus import Bus


class SchoolBus(School, Bus):
    def __init__(self, school_id, number_of_students, max_speed, mileage, seating_capacity, bus_school_color):
        School.__init__(self, school_id, number_of_students)
        Bus.__init__(self, max_speed, mileage, seating_capacity)
        self.bus_school_color = bus_school_color

    def bus_school_color(self):
        return self.bus_school_color
