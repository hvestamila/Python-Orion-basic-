# 12*. Making Your Objects Truthy or Falsey Using __bool__().
# Create class MyOrder with cart and customer instance attributes.
# Override the __bool__magic method considered to be truthy if the length of the cart list is non-zero.

class MyOrder:
    def __init__(self, cart, customer):
        # making cart private
        self.__cart = cart
        self.customer = customer

    def __bool__(self):
        return len(self.__cart) > 0
