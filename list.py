#list:mutable,ordered
#static
#my_list=[1,2,-13,41,2]
# my_list.append(9999)
#my_list.insert(8000,999)
#print(*my_list)
#print(len(my_list))
#my_list.pop(2)
#print(*my_list)
#my_list_2=[5,6,7,8]
#new_lst=my_list+my_list_2
#print(*new_lst)
#new_lst=my_list.copy()
#new_lst.pop()
#print(*new_lst)
#cnt=my_list.count(2)
#print(cnt)
#my_list.sort()
#print(*my_list)
#agg functions
# pop: default
#my_list.pop(4)
#4 represnts index count
#print(*my_list)
#my_list=list(map(int,input().split("@")))
#print(*my_list)
#my_list=list(map(str,input().split("@")))
#print(*my_list)
#list=["vai","shn","navi"]
#list.append("reddy")
# append: to add ssomething to the end of an existing list
#list.pop(1)
#print(*list)
list=list(map(int,input().split()))
print("1.append")
print("2.pop")
print("3.sort")
print("4.hello,len")
choice=int(input())
if(choice==1):
    list.append(2)
elif(choice==2):
    list.pop(1)
elif(choice==3):
    list.sort()
else:
    a=len(list)
    print(f"hello lenth is {a}")
    print(*list)