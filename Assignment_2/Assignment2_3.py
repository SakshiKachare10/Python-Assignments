def fact():
    n = int(input("Enter no : "))
    value = 1 
    for i in range(1,n+1):
        value *= i 
    print("factorial = ",value)
fact()


