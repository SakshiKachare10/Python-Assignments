def Factorial():
  # Function to calculate factorial of a number
  no = int(input("Enter a no:"))
  fact = 1
  for i in range(1,no+1):
    fact *= i
     
  print(fact)

def main():
  Factorial()

if __name__ == "__main__":
  main()    