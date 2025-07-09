from Num import CheckPrime, AcceptElements

def listPrime(numberList):
    sumPrime = 0
    listPrime = []
    for num in numberList :
        if(num>1) and CheckPrime(num):
            listPrime.append(num)
            sumPrime+=num

        print("Original list:",numberList)
        print("Prime no list:",listPrime)
        print(f"Addition of prime numbers in the list is :{sumPrime}")

def main():
    noOfElements = int(input("Enter number of elements in the list:"))
    inputNumberList = AcceptElements(noOfElements)
    listPrime(inputNumberList)

if __name__ == "__main__":
    main()    
