n=int(input("enter"))
a=n
t=n
count=0
sum=0
while(n!=0):
    rem = n%10
    count=count +1
    n=n//10
while(a!=0):
    z=a%10
    sum=sum+z**count
    a=a//10
if(sum==t):
    print("armstrong")
else:
    print("Not")