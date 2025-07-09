def MultiplicationTable():
  # Function to print multiplication table of a given number
  no = int(input("Enter a number:"))
  for i in range(1,11):
    print(no*i)

def main():
  MultiplicationTable()

if __name__ == "__main__":
  main()     
    
