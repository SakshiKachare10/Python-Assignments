def Add(value1,value2):
    result = value1 + value2
    return result

def Sub(value1,value2):
    result = value1 - value2
    return result

def Mult(value1,value2):
    result = value1 * value2
    return result

def Div(value1,value2):
    result = value1 / value2
    return result


    print("Enter number:")
    no = int(input())
    rows = no
    for i in range(1,rows + 1):
        for j in range(1,rows +1):
            if j<=i:
                print("*")
            else:
                print("*")     

        print()    