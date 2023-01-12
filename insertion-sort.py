input = input().split()
length = len(input)
for i in range (1,length):
    j=i
    while j>0 and int(input[j])<int(input[j-1]):
        k=input[j]
        input[j]=input[j-1]
        input[j-1]=k
        j=j-1
print(input)
