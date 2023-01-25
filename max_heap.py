class heap:
    def __init__(self,input_array):
        input_array.insert(0,0)
        self.input_array=input_array
        self.length=len(self.input_array)
        for i in reversed(range(1,self.length//2)):
            self.heapify_down(i)

    def heapify_up(self,i):
        if self.input_array[2*i]>self.input_array[2*i+1]:
            j=2*i
        else:
            j=2*i+1
        if self.input_array[i]<self.input_array[j]:
            self.input_array[i],self.input_array[j] = self.input_array[j],self.input_array[i]
            if i!=1:
                self.heapify_up(i//2)
        
    def heapify_down(self,i):
        have_one_child = (self.length%2==1) and (self.length//2==i)
        if (not have_one_child) and i>=self.length//2:
            return
        if have_one_child or self.input_array[2*i]>self.input_array[2*i+1]:
            j=2*i
        else:
            j=2*i+1
        if self.input_array[i]<self.input_array[j]:
            self.input_array[i],self.input_array[j] = self.input_array[j],self.input_array[i]
            self.heapify_down(j)

    def insert(self,value):
        self.input_array.insert(self.length-1,value)
        self.length=len(self.input_array)
        self.heapify_up((self.length-1)//2)

    def get_max(self):
        return self.input_array[1]

    def pop_max(self):
        max=self.get_max()
        self.input_array[self.length-1],self.input_array[1] = self.input_array[1],self.input_array[self.length-1]
        self.input_array.pop()
        self.length=self.length-1
        self.heapify_down(1)
        return max

    def arrayrobedeman(self):
        return self.input_array


input_array=list(map(int, input().split()))
my_heap=heap(input_array)
print(my_heap.arrayrobedeman())
my_heap.get_max()
my_heap.pop_max()
print(my_heap.arrayrobedeman())




