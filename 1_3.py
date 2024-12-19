# Write a Python program to print the series up to N terms: 1, 3,7, 13, 21, 31... and count the number of mathematical operators used without using any functions.
n=int(input("enter the number of terms::"))
a=1
d=2
count=2 #i,n
print(a,end=" ")
for i in range(n-1):
    a+=d
    d+=2
    print(f",{a}",end=" ")
    count+=2
print(f"\nno. of variables used ={count}")