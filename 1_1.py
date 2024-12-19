# Write a program in python to print all prime numbers inside a range of numbers provided by the user
x = int (input("enter first number:"))
y = int(input("enter last number:"))
for n in range (x,y+1):
    for i in range(2,n):
      if n%i ==0:
         break
    else:
      print(n)
         
