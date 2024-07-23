#find the maximum elements in the given list
#test case:0* 12 23 36 44 45 57 o/p57
#test case:1* 56 78 -8 12 34 -99 o/p78
'''my_list=list(map(int,input().split()))
for i in range(0,len(my_list)):
    if(my_list[i]<my_list[i+1]):
      print(my_list[i+1])
    else:
print(my_list[i])'''

my_list=list(map(int,input().split()))
maxi=my_list[0]
for i in range(len(my_list)):
    if(my_list[i]>maxi):
        maxi=my_list[i]
print(maxi)



