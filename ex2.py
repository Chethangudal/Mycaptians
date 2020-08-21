
n0 ,n1 = 0 ,1
n=int(input("enter the number of terms "))
if n == 0:
  print("enter the valid terms")
else:
    print("fibonacci series is")
    print(n0)
    print(n1)
    for i in range(n):
     n2=n0+n1
     print(n2)
     n0=n1
     n1=n2
        
    
    

