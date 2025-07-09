# Problem statement : Accept list of intgers from user and use reduce() function to find product of all numbers

from functools import reduce
Data = list()
size = 0
print("Enter no of elements:")
size = int(input())
print("Enter Elements:")
for  i in range(size):
    no = int(input())
    Data.append(no)

print(reduce(lambda A,B :A*B,Data))    