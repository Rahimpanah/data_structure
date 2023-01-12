
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
        X=self.head
        while (X):
            print(X.data)
            X=X.next

    def Insert_first(self, adding_value):
        temp=Node(adding_value)
        temp.next=self.head
        self.head=temp

    def Insert_last(self, adding_value):
        temp=Node(adding_value)
        self.last.next=temp
        self.last=temp

    def Delete_first(self):
        self.head=self.head.next
        self.head.previous=None

    def Delete_last(self):
        self.last=self.last.previous
        self.last.next=None
        




input=input().split()
length=len(input)
NewList=Linked_list()
NewList.head=Node(input[0])
NewList.last=NewList.head
for i in range (length-1):
    temp=NewList.last
    NewList.last.next=Node(input[i+1])
    NewList.last=NewList.last.next
    NewList.last.previous=temp

NewList.Delete_last()
NewList.PrintList()
    