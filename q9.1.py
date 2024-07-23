#print the element in the particular index element by cyclic printing find the element presint in k

'''n=[80,70,54,36,72,10,23]
k=20

for i in range(0,len(n)):
    if(k%7==0):
        print(i)
print(i)'''
my_list=list(map(int,input().split()))
k=int(input())
idx=k%len(my_list)
print(my_list[idx])
