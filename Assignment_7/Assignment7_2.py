# Problem statement : Accept list of intgers from user and use map() function to double each value

Data = list()
size = 0
print("Enter no of elements:")
size = int(input())
print("Enter Elements:")
for  i in range(size):
    no = int(input())
    Data.append(no)

print(list(map(lambda no : no *2 , Data)))