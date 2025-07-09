def CheckPrime(num):
    if num <= 1 :
        return False
    for cnt in range(2,num):
        if num % cnt == 0:
            return False
        return True


def main():
    number = int(input(("Enter a number to check for prime :")))
    isPrime = CheckPrime(number)      
    if (isPrime):
        print(f"{number} is a prime number")
    else:
        print(f"{number} is not a prime number")

if __name__ =="__main__":
    main()            