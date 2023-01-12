class heap:
    def __init__(self,input_array):
        input_array.insert(0,(0,0))
        self.input_array=input_array
        self.length=len(self.input_array)
        for i in reversed(range(2,self.length)):
            parent=i//2
            if self.input_array[parent][0] > self.input_array[i][0]:
                self.input_array[i],self.input_array[parent] = self.input_array[parent],self.input_array[i]

    def heapify_up(self,i):
        if self.input_array[2*i][0]<self.input_array[2*i+1][0]:
            j=2*i
        else:
            j=2*i+1
        if self.input_array[i][0]>self.input_array[j][0]:
            self.input_array[i],self.input_array[j] = self.input_array[j],self.input_array[i]
            if i!=1:
                self.heapify_up(i//2)
        
    def heapify_down(self,i):
        have_one_child = (self.length%2==1) and (self.length//2==i)
        if (not have_one_child) and i>=self.length//2:
            return
        if have_one_child or self.input_array[2*i][0]<self.input_array[2*i+1][0]:
            j=2*i
        else:
            j=2*i+1
        if self.input_array[i][0]>self.input_array[j][0]:
            self.input_array[i],self.input_array[j] = self.input_array[j],self.input_array[i]
            self.heapify_down(j)

    def insert(self,value):
        self.input_array.insert(self.length-1,value)
        self.length=len(self.input_array)
        self.heapify_up((self.length-1)//2)

    def get_min(self):
        return self.input_array[1]

    def pop_min(self):
        min=self.get_min()
        self.input_array[self.length-1],self.input_array[1] = self.input_array[1],self.input_array[self.length-1]
        self.input_array.pop()
        self.length=self.length-1
        self.heapify_down(1)
        return min

    def arrayrobedeman(self):
        return self.input_array

# if __name__=="__main__":
#     N=int(input())
#     input_array=[]
#     for i in range (N):
#         num, charc=input().split()
#         num=int(num)
#         input_array.append((num,charc))
#     my_heap=heap(input_array)
#     my_heap.pop_min()
#     print(my_heap.arrayrobedeman())
#     my_heap.pop_min()
#     print(my_heap.arrayrobedeman())
