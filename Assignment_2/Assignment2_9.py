def digits():
    no = int(input("Enter no:"))
    count = 0 
    while no > 0 :
        no = no // 10
        count += 1

    print(count)
digits()    