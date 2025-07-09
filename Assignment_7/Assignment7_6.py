# Problem statement : Accept list of intgers from user and use filter() function to find prime numbers from the list

def ChkPrime(number):
    if number<=1:
        return False
    for num in range(2,number):
         if (number % num == 0) :
                return False
    return True 

def acceptElements():
    nos=int(input("Enter the number of elements in the list:"))
    List =[]
    print(f"Enter the {nos} number to be added in the list:")
    for count in range(nos):
        number = int(input(f"Element({count+1}) : "))
        List.append(number)
    print("\nInput list elements are:",List)  
    return List 

def main():
    List=acceptElements()
    primeNumberList=list(filter(ChkPrime,List))
    print(f"\nPrime numbers list after filter():",primeNumberList)
  
if __name__ == "__main__":
     main()
