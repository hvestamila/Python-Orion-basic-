from collections import namedtuple
import dataclasses

print('# 1. Composition')


class Laptop:
    def __init__(self):
        battery_type_1 = Battery('This is laptop battery type 1')
        battery_type_2 = Battery('This is laptop battery type 2')
        battery_type_3 = Battery('This is laptop battery type 3')
        self.battery_types = [battery_type_1, battery_type_2, battery_type_3]


class Battery:
    def __init__(self, battery_type_text):
        self.battery_type_text = battery_type_text


# testing Composition
dell_laptop = Laptop()
for battery_type in range(len(dell_laptop.battery_types)):
    print('\t', dell_laptop.battery_types[battery_type].battery_type_text)

del dell_laptop

print('# 2. Aggregation')


class Guitar:
    def __init__(self, guitar_string):
        self.guitar_string = guitar_string


class GuitarString:
    def __init__(self):
        pass


guitar_string = GuitarString()
# guitar = Guitar(guitar_string)

print('\t', guitar_string)

print('# 3. Static method')


class Calc:

    def __init__(self):
        pass

    @staticmethod
    def add_nums(param_1, param_2, param_3):
        return param_1 + param_2 + param_3


calc_sum = Calc()
print('\t', calc_sum.add_nums(3, 4, 5))

print('# 4. Class method')


class Pasta:

    def __init__(self, ingredients):
        self.ingredients = ingredients

    @classmethod
    def carbonara(cls):
        carbonara_pizza = ['forcemeat', 'tomatoes']
        return cls(carbonara_pizza)

    @classmethod
    def bolognaise(cls):
        bolognaise_pizza = ['bacon', 'parmesan', 'eggs']
        return cls(bolognaise_pizza)


pasta_1 = Pasta(["tomato", "cucumber"])
print('\t', pasta_1.ingredients)

pasta_2 = Pasta.bolognaise()
print('\t', pasta_2.ingredients)

pasta_3 = Pasta.carbonara()
print('\t', pasta_3.ingredients)

print('# 5. Getter/Setter')

class Concert():

    max_visitors_num = 0

    def __init__(self):
        self._visitors_count = 0

    @property
    def visitors_count(self):
        return self._visitors_count

    @visitors_count.setter
    def visitors_count(self, v_count):
        if v_count >= Concert.max_visitors_num:
            self._visitors_count = Concert.max_visitors_num
        else:
            self._visitors_count = v_count

print('\t Before: ', Concert.max_visitors_num)
Concert.max_visitors_num = 50
print('\t After: ', Concert.max_visitors_num)

concert = Concert()
concert.visitors_count = 1000
print('\t Visitors count if max_visitors_num less than visitors_count: ', concert.visitors_count)  # 50
concert.visitors_count = 49
print('\t Visitors count if max_visitors_num greater than visitors_count:: ', concert.visitors_count)  # 49

print('# 6. Dataclasses')

@dataclasses.dataclass
class AddressBookDataClass:
    key: int
    name: str
    phone_number: str
    address: str
    email: str
    birthday: str
    age: int

my_address = AddressBookDataClass(1, 'MyAddress', '380636384848', 'Chervonoyii Kalyny', 'hves.tamila@gmail.com', '07/07/1995', 26)
print('\t', my_address.address)

print('# 7. NamedTuple')

AddressBookNamedTuple = namedtuple('AddressBook', ['key', 'name', 'phone_number', 'address', 'email', 'birthday', 'age'])
my_address = AddressBookNamedTuple(1, 'MyAddress', '380636384848', 'Chervonoyii Kalyny', 'hves.tamila@gmail.com', '07/07/1995', 26)
print('\t', my_address.name)
print('\t', my_address[3])
print('\t', str(my_address))

print('# 8. Str override')
class AddressBook:

    def __init__(self, key, name, phone_number, address, email, birthday, age):
        self.key = key
        self.name = name
        self.phone_number = phone_number
        self.address = address
        self.email = email
        self.birthday = birthday
        self.age = age

    def __str__(self):
        return f"{AddressBook.__name__}(key={self.key}, " \
               f"name='{self.name}', phone_number='{self.phone_number}', " \
               f"address='{self.address}', email='{self.email}', " \
               f"birthday='{self.birthday}', age={self.age})"

my_address_str = AddressBook(1, 'MyAddress', '380636384848', 'Chervonoyii Kalyny', 'hves.tamila@gmail.com', '07/07/1995', 26)
print('\t', str(my_address_str))

print('# 9. Override attribute value')

class Person:

    def __init__(self, name, country):
        self.name = name
        self.country = country

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age_num):
        age_num = 31
        self._age = age_num


john = Person('John', 'USA')
john.age = 41
print('\t', john.age)

print('# 10. getattr() and setattr()')
class Student:

    id = 0
    name = ""
    student_email = ''

    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email

elli = Student(1, 'Elli', 'elli@gmail.com')

setattr(elli, 'student_email', elli.email)
print('\t Student email is: ', getattr(elli, 'student_email'))

print('# 11. ')
class Celsius:
    """
    By using @property convert the celsius to fahrenheit
    Hint: (temperature * 1.8) + 32)
    """
    def __init__(self, temperature=0):
        self._temperature = temperature

    @property
    def temperature(self):
        return (self._temperature * 1.8) + 32

summer_temp = Celsius(28)
print('\t', summer_temp.temperature)
