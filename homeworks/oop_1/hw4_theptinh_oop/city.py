# 8. Create class City with name, population instance attributes, return a new instance only when population > 1500,
# otherwise return message: "Your city is too small".

class City:
    def __new__(cls, name, population, budget=None):
        if population > 1500:
            instance = super(City, cls).__new__(cls)
            instance.__init__(name, population, budget)
            return instance
        else:
            return 'Your city is too small'

    def __init__(self, name, population, budget=None):
        self.city_name = name
        self.city_population = population
        self.__budget = budget

    def __str__(self):
        return f'The population of the city {self.city_name} is {self.city_population}'

    def get_budget(self):
        return self.__budget

    def set_budget(self, budget):
        self.__budget = budget
