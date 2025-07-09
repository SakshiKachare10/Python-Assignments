def pattern():

    n = int(input("Enter the number of rows required:"))
    for i in range(n):
        for j in range(n):
            print("*",end = '  ')
        print()

pattern()            