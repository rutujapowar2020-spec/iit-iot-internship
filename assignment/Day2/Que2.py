
num=(input("Enter digit number:" ))
i=len(num)
print("Length of num =",i)
k=0
m=int(num)
y=int(num)
while y>0:
   j=y%10
   k=k*10+j
   y//=10
  
if m==k:
     print(m,"Number is Palindrome")
else:
     print(m,"Number is not Palindrome")
