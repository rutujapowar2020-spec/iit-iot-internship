
    #a=0,b=1 0+1=1+1=2+1=3+2=5+3=8
# Without function

"""num=int(input("Enter number:"))
k=0
i=1
j=0
for j in range(num):
    print(k)
    a=k
    k=i+k
    i=a
    j+=1"""
    

# With Function
    
    
def fibonacci(n):
    a, b = 0, 1
    print("Fibonacci Series:")
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

num= int(input("Enter number of num: "))
fibonacci(num)
