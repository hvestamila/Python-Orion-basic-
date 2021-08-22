import logging
from datetime import date
import pprint as pp

# class Calc:
filename = str(date.today()) + '.log'
template = "%(levelname)s: %(filename)s: %(asctime)s - %(message)s"

logging.basicConfig(filename=filename, level=logging.INFO, format=template, filemode="a")


def add(a, b):
    return a + b


def substract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def power(a, b):
    return pow(a, b)


def root(a, b):
    return a ** (1.0 / b)


def percentage(a, b):
    return 100 * float(a) / float(b)


operations = {
    1: add,
    2: substract,
    3: multiply,
    4: divide,
    6: root,
    5: power,
    7: percentage
}

def calc():
    while True:
        a = int(input('Please enter number 1: '))
        pp.pprint(operations)
        operation = int(input('Please enter operation type: '))
        b = int(input('Please enter number 2: '))
        print(operations[operation](a, b))


calc()