#take a space separated input from a user and print alternate elements
list=list(map(int,input("enter numbers").split(" ")))
for i in range(0,len(list),2):
    print(list[i])
    