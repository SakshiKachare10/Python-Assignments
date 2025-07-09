#CheckNo = lambda no : (no>=70,no<=90)
from functools import reduce
# AddNo = lambda no : (no + 10)
#MultNo = lambda A,B : A*B

def List():

   print("Enter no of elements:")
   size = int(input())

   
   Data = list()
   print("Enter numbers:")
   for i in range(size):
      no = int(input())
      Data.append(no)

   print("Input Data:",Data)

   FData = list(filter( lambda no : (90>=no>=70),Data))
   print("list after filter:",FData)

   MData = list(map(lambda no : (no + 10),FData))
   print("list after map:",MData)

   RData = reduce(lambda A,B: A*B ,MData)
   print("Output of reduce:",RData)
      

List()
   

   

