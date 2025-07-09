def Addition():
    print("Enter number of elements:")
    size = int(input())

    Data = list()

    print("Enter the values:")
    for i in range(size):
        no = int(input())
        Data.append(no)

    print("Addition of nos is :")
    sum = 0
    for i in Data:
        sum += i
    print(sum)


Addition()        

