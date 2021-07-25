from _datetime import datetime, date

# file = open(r"text_file.txt", "r")
# file = open(r"text_file.txt", "r+")
# file = open(r"text_file.txt", "w")
# file = open(r"text_file.txt", "x") # exists
# file = open(r"text_file.txt", "a") # append

# ACCESS TO TXT FILES

# file = open(r"text_file.txt", "r+")
# print(type(file))
# print(file.read())
# print(file.readlines())
# print(file.readline())
# file.write("\nWritten text")




# ACCESS TO BINARY FILES
# file = open(r"purple_flower.jpeg", "rb")
# # print(file.read())
# img_data = file.read()
# file.close()
# file = open(r"purple_flower_copy.jpeg", "wb")
# file.write(img_data)
# file.close()

# WORKING WITH pickle
# import pickle
#
# lst_1 = [1, 2, 3, 4, 5]
#
# # METHODS:
# # pickle.load()
# # pickle.loads()
# # pickle.dumps()
# # pickle.dump()
#
# print(pickle.dumps(lst_1))
#
# serialized_data = pickle.dumps(lst_1)
# deserialized_data = pickle.loads(serialized_data)
#
# print(deserialized_data)
#
# # file = open("list.txt", "wb")
# # pickle.dump(lst_1, file)
#
#
# file = open("list.txt", "rb")
# obj = pickle.load(file)
# print(obj)
# file.close()
#

# with open("text_file.txt", "r") as file, open("text_file_copy.txt", "r") as file_copy:
#     print(file.read())
#     print('\nCopy file:')
#     print(file_copy.read())

# name = 'Tamila'
# date = datetime.now()
#
# with open("text_file.txt", "r") as file:
#     # txt_data = file.read()
#     # # print(type(txt_data))
#     # print(txt_data)
#
#     template = file.read()
#     file_created = template.format(name, date)
#
# print(file_created)

# CONTEXT MANAGER WITH ENTER AND EXIT METHODS
# class MyOpen:
#
#     def __init__(self, path, access_atr = 'r'):
#         self.file = open(path, access_atr)
#
#     def __enter__(self):
#         return self.file
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         # print(exc_type, exc_val, exc_tb)
#         if exc_type is None:
#             self.file.close()
#         elif exc_type is Exception:
#             print('Exception is thrown')
#             return True
#             # if there was an exception, make backup
#
# with open("text_file.txt", "r") as file:
#     print(file.read())
#
# with MyOpen("text_file.txt", "r") as file:
#     print(file.read())
#     raise Exception


# class Connection:
#
#     def __init__(self):
#         self.connection = None
#
#     def __enter__(self):
#         return self.connection
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         if exc_type is None:
#             return True
#         elif exc_type is DBMergeConflict:
#             return True
#         ...
#         else:
#             return False


class Vec3f:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        self.x += other
        self.y += other
        self.z += other
        return self

    def __mul__(self, other):
        self.x *= other
        self.y *= other
        self.z *= other
        return self

    def __save(self):
        self.x = self.__temp_vector.x
        self.y = self.__temp_vector.y
        self.z = self.__temp_vector.z

    def __str__(self):
        return f'{self.x}; {self.y}; {self.z}'

    def __enter__(self):
        self.__temp_vector = Vec3f(self.x, self.y, self.z)
        return self.__temp_vector

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.__save()
        elif exc_type is TypeError:
            self.__temp_vector = None
            return True
        else:
            return False

vec_1 = Vec3f(1, 2, 3)

with vec_1 as vec:
    print(vec)
    vec += 1
    print(vec)
    vec *= 3
    print(vec)
    vec += '1'
    # raise ZeroDivisionError

print(vec_1)