def ChkEligibility():
    age = int(input("Enter age:"))
    if age < 18:
        print("Not eligible to vote")
    else:
        print("Eligible to vote")    

ChkEligibility()        