def prime():
    no = int(input("Enter no : "))
    if no == 1 or no == 0:
        print("Its not prime no") 
    elif no > 1:
        for i in range(2,no):
            if no % i == 0:
              print("Its not prime no")
              break 
        else:
            print("Its prime no")  
    else:
        print("Its prime no ")
                
     

prime()                
        

             