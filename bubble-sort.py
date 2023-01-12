input= input().split()
n = len(input)
for i in range(0,n-1):
    sw=False
    for j in range(0,n-1-i):
        if int(input[j])>int(input[j+1]):
            k=input[j]
            input[j]=input[j+1]
            input[j+1]=k
            sw=True
    if sw==False:
        break
print(input)
