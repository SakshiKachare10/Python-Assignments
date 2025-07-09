def pattern():
    n = int(input("Enter no of rows required: "))
    for i in range(n+1):
        for j in range(1,i+1):
            print(j,end = "  ") 
        print()

pattern() 

