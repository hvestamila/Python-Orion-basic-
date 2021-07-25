import re

subtitles_dict = {}

with open("task1.txt", "r") as subtitle_file:
    for line in subtitle_file:
        nextLine = next(subtitle_file)
        subtitles_dict[line.strip()] = nextLine.strip()

print('Task 1: ', subtitles_dict, '\n')

# file = open("task1.txt", "r")
# data = file.read()
# file_copy = open("task1_copy.txt", "w")
# file_copy.write(data)

file_copy = open("task1_result.txt", "r+")

# APPROACH 1
with open("task1_copy.txt", "r") as subtitle_file_copy:
    for line in subtitle_file_copy:
        if line[0].isalpha():
            file_copy.write(line.strip().replace('.', '. '))

for line in file_copy:
    print('Task 2 (Approach 1):', line, '\n')

# # APPROACH 2
# with open("task1_copy.txt", "r+") as subtitle_file_copy:
#     input = subtitle_file_copy.readlines()
#     subtitle_file_copy.seek(0, 0)
#     for line in input:
#         # if line[0].isdigit():
#         if re.match('\d{2}:\d{2}', line):
#             input.pop(input.index(line))
#
#     print(input)

with open("task2", "r") as file_2:
    for line in file_2:
        print(line)
