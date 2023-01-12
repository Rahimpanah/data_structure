def merge(A,B):
    lengthA=len(A)
    lengthB=len(B)
    C=[None]*(lengthA+lengthB)
    i=0
    j=0
    k=0
    while (i<lengthA) or (j<lengthB):
        if i==lengthA:
            C[k]=B[j]
            j=j+1
        elif j==lengthB:
            C[k]=A[i]
            i=i+1        
        elif int(A[i])<int(B[j]):
            C[k]=A[i]
            i=i+1
        elif int(B[j])<=int(A[i]):
            C[k]=B[j]
            j=j+1
        k=k+1
    return C

def sort(I,p,r):
    if p<r-1:
        if (p+r)%2==0:
            q=int((p+r)/2)
        else:
            q=((p+r)//2)+1
        X=sort(I,p,q)
        Y=sort(I,q,r)
        return merge(X,Y)
    else:
        return I[p:r]

input=input().split()
p=0
r=len(input)
sorted_array=sort(input,p,r)
print(sorted_array)