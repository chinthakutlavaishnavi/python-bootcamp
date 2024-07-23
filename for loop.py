1#find sum of all the nos using for loop
2#print nos 1to100 using for loop
3#append 1to 100 in empty list
1#for i in range(1,101):
   # print(i)

2#n=100
#for i in range(1,n+1): 
#    print(i,end=" ")

#que2:
n=int(input("enter nth value"))
list1=[]
for i in range(1,n+1):
    list1.append(i)
print(*list1)
