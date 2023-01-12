def sort(I,p,r):
    pivot=r
    if p>=r:
        return
    i=p
    while pivot>i:
        if I[i]>I[pivot]:
            k=I[i]
            I[i]=I[pivot-1]
            I[pivot-1]=I[pivot]
            I[pivot]=k
            pivot=pivot-1
        else:
            i=i+1
    sort(I,p,pivot-1)
    sort(I,pivot+1,r)
    return I

input=input().split()
p=0
r=len(input)-1
integer_input=list(map(int, input))
output=sort(integer_input,p,r)
print(output)
