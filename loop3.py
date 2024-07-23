strng1=list(map(str,input("enter strings").split(" ")))
#method1
for i in range(len(strng1)):
    print(strng1[i],end=" ")
print("\n")    
#method2:-
for i in strng1:
    print(i,end=" ")