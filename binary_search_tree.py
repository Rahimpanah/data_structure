class Node:
    def __init__(self):
        self.value=None
        self.right_children=None
        self.left_children=None
        self.parent=None

class binary_tree:
    def __init__(self):
        self.root=self.get_Node()
    
    def get_Node(self):
        return Node()

    def insert(self,element,current_node=None):
        if current_node==None:
            current_node=self.root
        
        if element>current_node.value:
            if current_node.right_children==None:
                new_node=self.get_Node()
                new_node.value=element
                new_node.parent=current_node
                current_node.right_children=new_node
                return True
            else:
                return self.insert(element,current_node=current_node.right_children)

        elif element<current_node.value:
            if current_node.left_children==None:
                new_node=self.get_Node()
                new_node.value=element
                new_node.parent=current_node
                current_node.left_children=new_node
                return True
            else:
                return self.insert(element,current_node=current_node.left_children)
        return False

    def search(self,value,current_node=None):
        if current_node==None:
            current_node=self.root
        if value>current_node.value:
            if current_node.right_children==None:
                return None
            else:
                return self.search(value,current_node=current_node.right_children)
        elif value<current_node.value:
            if current_node.left_children==None:
                return None
            else:
                return self.search(value,current_node=current_node.left_children)
        return current_node

    def is_right_child(self,node):
        if node.parent.right_children==node:
            return True
        return False
    
    def is_left_child(self,node):
        if node.parent.left_children==node:
            return True
        return False
    
    def find_successor(self,element_node):
        if element_node.right_children==None:
            if self.is_left_child(element_node):
                return element_node.parent
            elif self.is_right_child(element_node):
                next_node=element_node.parent
                while self.is_right_child(next_node):
                    next_node=next_node.parent
                if self.is_left_child(next_node):
                    return next_node.parent
                else:
                    return None
        else:
            next_node=element_node.right_children
            while next_node.left_children!=None:
                next_node=next_node.left_children
            return next_node

    def delete(self,value):
        delete_node=self.search(value)
        if delete_node!=0:
            self.final_delete(delete_node)
    
    def final_delete(self,delete_node):
        if delete_node.right_children==None and delete_node.left_children==None:
            if self.is_right_child(delete_node):
                delete_node.parent.right_children=None
            else:
                delete_node.parent.left_children=None
        elif delete_node.left_children != None and delete_node.right_children != None:
            successor = self.find_successor(delete_node)
            delete_node.value = successor.value
            self.final_delete(successor)
        elif delete_node.left_children!=None:
            if delete_node==self.root:
                delete_node.left_children.parent=None
                self.root=delete_node.left_children
            else:
                if self.is_left_child(delete_node):
                    delete_node.parent.left_children=delete_node.left_children
                else:
                    delete_node.parent.right_children=delete_node.left_children
                delete_node.left_children.parent=delete_node.parent
        elif delete_node.right_children!=None:
            if delete_node==self.root:
                delete_node.right_children.parent=None
                self.root=delete_node.right_children
            else:
                if self.is_right_child(delete_node):
                    delete_node.parent.right_children=delete_node.right_children
                else:
                    delete_node.parent.left_children=delete_node.right_children
                delete_node.right_children.parent=delete_node.parent
        return

input_elements=[4,10,12,21,4,24]
BT=binary_tree()
BT.root.value=input_elements[0]
length=len(input_elements)
for i in range (1, length):
    BT.insert(input_elements[i])
BT.delete(12)
result=BT.search(12)
if result==1:
    print("YES")
else:
    print("NO")
# search_elements=[22,1,24,4,9,33]
# for i in search_elements:
#     result=BT.search(i)
#     if result==1:
#         print("YES")
#     else:
#         print("NO")


