def pattern():
    n = int(input("Enter the number of rows required : "))
    for i in range(1,n+1):
        for j in range(1,n+1):
            print(j,end = "  ")
        print()

pattern()        



