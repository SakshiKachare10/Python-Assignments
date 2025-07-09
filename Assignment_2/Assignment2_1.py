from Arithmetic import Add, Sub, Mult, Div 

print("Enter 1st number:")
no1 = int(input())

print("Enter 2nd number")
no2 = int(input())

ans = Add(no1,no2)
print("Addition is :",ans)

ans = Sub(no1,no2)
print("Substraction is :",ans)

ans = Mult(no1,no2)
print("Multiplication is :",ans)

ans = Div(no1,no2)
print("Division is :",ans)

