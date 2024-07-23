#find the sum of squares  of given numbers
n=123
sum=0
while n>0:
    r=n%10 #n= 1 2 3
    sum=sum+r**2 #r**2
    n=n//10
print(sum)