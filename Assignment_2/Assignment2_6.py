def pattern():
    n = int(input("Enter the no of rows required: "))
    for i in range(n):
        for j in range(i,n):
            print("*",end = "  ")
        print()

pattern()        

