#12 23 36 44 45 57
#123 into reverse 321
n=1234
'''rev=""
while n>0:
    r=n%10
    rev=rev+str(r)
    n=n//10
print(int(rev))'''
rev=""
while n>0:
    r=n%10
    rev=rev+str(r)
    n=n//10
    ans=int(rev)
print(ans)
print(type(ans))