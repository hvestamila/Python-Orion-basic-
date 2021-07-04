from bus import Bus
from vehicle import Vehicle
from bear import Bear
from wolf import Wolf
from school import School
from school_bus import SchoolBus
from city import City
from call_sum import Sum
from my_order import MyOrder
import inspect

if inspect.isclass(Vehicle):
    print('# 1. Vehicle class created with the following methods: \n   ', sorted(dir(Vehicle), reverse=True))

if inspect.isclass(Bus):
    print('# 2. Bus class created with the following methods: \n   ', sorted(dir(Bus), reverse=True))

# 3. Determine which class a given Bus object belongs to (Check type of an object)
# from bus import Bus
airport_bus = Bus(80, 90000, 22)
print('# 3: ', type(airport_bus))

# 4. Determine if School_bus is also an instance of the Vehicle class
School_bus = Bus(70, 90000, 34)
print('# 4: ', isinstance(School_bus, Vehicle))

if inspect.isclass(School):
    print('# 5. School class created with the following methods: \n   ', sorted(dir(School), reverse=True))

if inspect.isclass(SchoolBus):
    print('# 6. SchoolBus class created with the following methods: \n   ', sorted(dir(SchoolBus), reverse=True))

# 7. Polymorphism: Create two classes: Bear, Wolf. Both of them should have make_sound method.
# Create two instances, one of Bear and one of Wolf,
# make a tuple of it and by using for call their action using the same method.
white_bear = Bear('Growl!')
arctic_wolf = Wolf('Howl!')

print('# 7: ')
for animal in (white_bear, arctic_wolf):
    print(animal.make_sound())

# 8. Create class City with name, population instance attributes, return a new instance only when population > 1500,
# otherwise return message: "Your city is too small".
print('# 8:')
london = City('London', 20000)
print(london)

kyiv = City('Kyiv', 100)
print(kyiv)

# Set value into private attribute
london.set_budget(23424311434)
print(london.get_budget())
london._City__budget = 2982989101
print(london._City__budget)

# 9. Override a printable string representation of the City class
# and return: The population of the city {name} is {population}


# 11. The __call__ method enables Python programmers to write classes
# where the instances behave like functions and can be called like a function.
# Create a new class with __call__ method and define this call to return sum.
find_sum = Sum(1)
print('# 11: ', find_sum(4, 5))

# 12*. Making Your Objects Truthy or Falsey Using __bool__().
order_1 = MyOrder(['a', 'b', 'c'], 'd')
print(bool(order_1))

order_2 = MyOrder([], 'a')
print(bool(order_2))
