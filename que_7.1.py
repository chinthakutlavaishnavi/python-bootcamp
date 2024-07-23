#7.3que:your give with a space separated integer list find number of foreven and odd elements in a
list1=list(map(int,input().split(",")))
even=0
odd=0
for i in range(len(list1)):
    if list1[i]%2==0:
        even+=1
    else:
        odd+=1
print(even)
print(odd)

#que7.2:to count number of evev and odd elements
#count=0
list1=list(map(int,input().split(",")))
for i in range(1,len(list1),2):
    #if(list1[i]%2==0):
      #print(list1[i])
 count+=1
print(count)