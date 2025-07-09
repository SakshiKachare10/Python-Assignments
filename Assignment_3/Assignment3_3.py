def Min():
    print("Enter no of elements:")
    size = int(input())

    Data = list()

    print("Elements are:")
    for i in range(size):
        no = int(input())
        Data.append(no)

    print("Minimun no in list :")
    print(min(Data))    

Min()    