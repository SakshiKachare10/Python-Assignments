# Problem statement : This program checks if given string is palindrome or not

def Palindrome():
    string = input("Enter a string:")
    rev = ""
    for char in string:
        char = char + rev
    if string == rev:
        print("String is pallindrome")
    else:
        print("String is not pallindrome")

Palindrome()                

