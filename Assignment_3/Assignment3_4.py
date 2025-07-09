def Freq():
    print("Enter no of elements:")
    size = int(input())

    Data = list()

    print("Enter nos:")
    for i in range(size):
        no = int(input())
        Data.append(no)

    freq_list = {}
    for i in Data:
        if i in freq_list:
           freq_list += 1
        else:
           freq_list = 1
    print(freq_list)        
        


Freq()

            

