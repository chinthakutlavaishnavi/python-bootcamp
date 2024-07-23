'''n=[4,5,7,8,9,34]
k=3
my_list=list(map(int,input().split()))
for i in range(0,len(my_list)):
    print(my_list[k+N],end="")
    break'''
n=[3,6,8,4,61,2]
k=3
N=2
for i in range(0,len(n)):
    if(i==k+n):
        print(n[i])