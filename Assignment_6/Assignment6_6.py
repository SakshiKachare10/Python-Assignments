def PrintStars(num):
    for row in range(num):
        for column in range(num):
            if(row>=column):
                print("*",end =" ")
        print()


def main():
    number = int(input("Enter no of lines to print stars:"))
    PrintStars(number)

if __name__ == "__main__":
    main()               
            