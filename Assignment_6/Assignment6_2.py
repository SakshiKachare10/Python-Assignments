def sum_of_even_numbers():
  sum = 0
  for i in range(1,101):
    if i % 2 == 0:
        sum += i
  print("sum of even numbers between 1 to 100 is:",sum)

def  main():
    sum_of_even_numbers()

if __name__ == "__main__":
   main()    