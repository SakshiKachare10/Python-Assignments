def Max():
    print("Enter number of elements:")
    size = int(input())

    Data = list()

    print("Elements are:")
    for i in range(size):
        no = int(input())
        Data.append(no) 
    
    print("Maximum no in list:")
    print(max(Data))

Max()