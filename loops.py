my_list=list(map(int,input("enter list values").split()))
for i in range(len(my_list)):
       print(my_list[i],end=" ")#prints values in newlist
       print("\n---------------")
for i in my_list:
    print(i,end="")#prints index of each values
