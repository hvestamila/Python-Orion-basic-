# 11. The __call__ method enables Python programmers to write classes
# where the instances behave like functions and can be called like a function.
# Create a new class with __call__ method and define this call to return sum.

class Sum:

    def __init__(self, num_3):
        self.num_3 = num_3

    def __call__(self, num_1, num_2):
        return num_1 + num_2 + self.num_3
