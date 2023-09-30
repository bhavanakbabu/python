num=int(input("enter a number:"))
factorial=1
if(num<0):
    print("factorial does not exist for -ve numbers")
elif(num==0):
    print("the factorial is zero is one")
else:
    for i in range(1,num+1):
        factorial=factorial*i
    print("the factorial is",factorial)
        
