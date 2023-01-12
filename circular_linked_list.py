class Node:
    def __init__(self, data):
        self.data=data
        self.next=None
        self.previous=None

class Linked_list:
    def __init__(self):
        self.head=None
        self.last=None
    
    def PrintList(self):
        x=self.head
        y=self.head.previous
        while(x!=y):
            print(x.data)
            x=x.next
        print(y.data)

    def Insert_last(self, adding_value):
        temp=Node(adding_value)
        x=self.last
        self.last.next=temp
        self.last=temp
        self.last.previous=x
        self.last.next=self.head
        self.head.previous=self.last
    
    def Delete_Node(self, input_Node):
        front=input_Node.next
        back=input_Node.previous
        front.previous=back
        back.next=front
        if (input_Node==self.head):
            self.head=front
        if (input_Node==self.last):
            self.last=back

input=input().split()
length=len(input)
NewList=Linked_list()
NewList.head=Node(input[0])
NewList.last=NewList.head
for i in range (1, length):
    NewList.Insert_last(input[i])
x=NewList.head
while(NewList.head!=NewList.last):
    NewList.Delete_Node(x.next)
    x=x.next
NewList.PrintList()
