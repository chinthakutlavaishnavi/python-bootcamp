#replace the elements in array to the average of maximum and minimum elements:0:o/p:13 2 67 20 68:
#min=2,max=68,min+max=70==35,35 35 35 35 
my_list=list(map(int,input().split()))
max=my_list[0]
for i in range(len(my_list)):
    if(my_list[i]>max):
        max=my_list[i]
    #print(max)
min=my_list[0]
for i in range(len(my_list)):
      if(my_list[i]>max):
        min=my_list[i]
avg=(max+min)/2
for i in range(len(my_list)):
    my_list[i]=avg
print(my_list)
'''my_list=list(map(int,input("enter values").split()))
max=my_list[0]
for i in range(len(my_list)):
    if(my_list[i]>max):
        max=my_list[i]
    #print(max)
min=my_list[0]
for i in range(len(my_list)):
      if(my_list[i]>max):
        min=my_list[i]
avg=(max+min)/2
for i in range(len(my_list)):
    my_list[i]=avg
print(my_list)'''







