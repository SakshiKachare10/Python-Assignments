from functools import reduce
ChkEven = lambda no : (no % 2 == 0)
Square = lambda no : (no** 2) 
Add = lambda A,B: A+B 

def FMR():

    print("Enter no of elements:")
    size = int(input())

    Data = list()

    print("Enter elements:")
    for i in range(size):
        no = int(input())
        Data.append(no)

    print("Input Data:",Data)

    FData = list(filter(ChkEven,Data))
    print("list after filter:",FData)

    MData = list(map(Square,FData))
    print("list after map:",MData)

    RData = reduce(Add,MData)
    print("Output of reduce:",RData)


FMR()        
