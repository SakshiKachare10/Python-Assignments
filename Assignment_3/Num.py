def CheckPrime(number):
    isPrime = True
    for num in range(2,number):
        if (number % num == 0):
            isPrime = False
            break
    return isPrime


def AcceptElements(noOfElements):
    inputNumberList = []
    print(f"Enter the {noOfElements} number to be added in the list:")
    for count in range(noOfElements):
        number = int(input(f"Element({count +1})"))
        inputNumberList.append(number)
    print("Input Elements list is:",inputNumberList)
    return inputNumberList    