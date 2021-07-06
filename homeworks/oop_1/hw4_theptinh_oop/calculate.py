# 10*. Override magic method __add__() to perform the additional action as 'multiply' (*)
# the value which is greater than 10. And perform this add (+) of two instances.
class Calculate:
    def __init__(self, x):
        self.x = x

    def __add__(self, other):
        if other.x > 10 or self.x > 10:
            return self.x * other.x
        else:
            return self.x + other.x
