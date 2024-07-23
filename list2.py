list=list(map(int,input().split()))
print("1.append")
print("2.pop")
print("3.sort")
print("4.hello,length")
choice=int(input())
if(choice==1):
    list.append(2)
elif(choice==2):
    list.pop(1) 
elif(choice==3):
    list.sort() 
else:
    a=len(list)
    print(f"hello length is {a}")   
print(*list)