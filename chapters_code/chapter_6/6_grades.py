import math
from math import ceil
num = int(input('enter the marks'))
# print(ceil(num/10)*10)
grades = ['F', 'F', 'F', 'F', 'F', 'D', 'C', 'B', 'A', 'EX']
index = ceil(num/10)
if index >= 5:
    print(f"the grade is {grades[index-1]}")
else:
    print(f"the grade is {grades[0]}")
