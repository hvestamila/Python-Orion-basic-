import pickle
import openpyxl
from openpyxl.utils.exceptions import InvalidFileException

'''
1. словник елементами якого буде пара ключ:значення 
де ключ - мітка часу, значення - репліка в даний момент часу
'''
subtitles_dict = {}

with open("task1.txt", "r") as subtitle_file:
    for line in subtitle_file:
        nextLine = next(subtitle_file)
        subtitles_dict[line.strip()] = nextLine.strip()

print('Task 1: ', subtitles_dict, '\n')

file = open("task1.txt", "r")
data = file.read()
file_copy = open("task1_copy.txt", "w")
file_copy.write(data)

file_copy = open("task1_result.txt", "r+")

'''
2. файл в якому знаходиться текст 
з якого видалені всі мітки часу.
 всі субтитри повинні мати вигляд простого тексту.
'''
with open("task1_copy.txt", "r") as subtitle_file_copy:
    for line in subtitle_file_copy:
        if line[0].isalpha():
            file_copy.write(line.strip().replace('.', '. '))

for line in file_copy:
    print('Task 2: ', line, '\n')

'''
Task 2
в файлі task2 збережений список, відкрийте цей файл, 
прочитайте вміст, і знайдіть середнє арифметичне чисел 
що знаходяться в списку
'''
with open("task2", "rb") as file_2:
    lst = pickle.load(file_2)
    print(lst)
    avg = round(sum(lst) / len(lst), 2)
    print(avg)

'''
Task 3
Використовуючи openpyxl (або будь-яку іншу зручну для вас бібліотеку), 
напишіть контекстний менеджер для роботи з ексель.
Даний менеджер повинен бути аналогом методу open()
'''


class MyExcelOpen:

    def __init__(self, path, read_only=True):
        try:
            self.file = openpyxl.load_workbook(path, read_only)
        except InvalidFileException:
            print('WRONG FILE FORMAT.')

    def __enter__(self):
        if hasattr(self, 'file'):
            return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Exception Type: ', exc_type, 'Exception Value: ', exc_val, 'Exception Traceback: ', exc_tb)
        if exc_type is None and hasattr(self, 'file'):
            self.file.close()
        elif exc_type is Exception:
            print('Exception is thrown')
            return True


with MyExcelOpen('SampleData.xlsx') as file:
    if file:
        sheet = file.active
        for row in sheet.values:
            for value in row:
                print(value)

with MyExcelOpen("task2") as file:
    if file:
        sheet = file.active
        for row in sheet.values:
            for value in row:
                print(value)
