# Problem statement : Accept list of intgers from user and use filter() function to  keep only even numbers

Data = list()
size = 0
print("Enter no of elements:")
size = int(input())
print("Enter Elements:")
for  i in range(size):
    no = int(input())
    Data.append(no)

print(list(filter(lambda no : no %2 == 0,Data)))    