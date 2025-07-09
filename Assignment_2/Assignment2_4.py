def factor():
    n = int(input("Enter no: "))
    factor = 0
    for i in range(1,n):
        if n % i == 0:
            factor += i
    print("addition of factors is:",factor)
factor()

