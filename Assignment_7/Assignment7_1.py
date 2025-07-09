def Calculate():
    # This function calculates the square and cube of a number
    Square = lambda no : no**2
    Cube = lambda no : no**3
    no = int(input("Enter a number:"))
    ret1 = Square(no)
    print("Square:",ret1)
    ret2 = Cube(no)
    print("Cube:",ret2)

def main():
    Calculate()

if __name__ == "__main__":
    main()        
