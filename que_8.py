#given an space separated integer  list ,find the average of elemnts presnt in the even index
list4=list(map(int,input().split(",")))
total=0
lenth=len(list4)-1
for i in list4:
    if i%2==0:
        total+=i
average=total/lenth
print(average)
#method2:
my_list=list(map(int,input().split(",")))
sum=0
n=len(my_list)
for i in range(len(my_list)):
 if(i%2==0):
    sum+=my_list[i]
    
    print(sum/n)

    #method3:using count
    my_list=list(map(int,input().split(",")))
    sum=0
    count=0
    n=len(my_list)
for i in range(len(my_list)):
   sum+=my_list[i]
   count+=1

   print(sum/count)

