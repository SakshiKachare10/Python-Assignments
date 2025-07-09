def add_digits():
    no = int(input("Enter no :"))
    sum = 0
    while no > 0 :
      sum += no % 10
      no = no // 10
    print("Addtion of digits is:",sum)

add_digits()    

