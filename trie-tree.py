class TrieNode:
    def __init__(self):
        self.children=[None for _ in range(26)]
        self.IsEndOfWord=False
        self.NumOfVisit=0

class Trie:
    def __init__(self):
        self.root=self.getNode()

    def getNode(self):
        return TrieNode()

    def char_position(self,letter):
        return ord(letter) - 97

    def insert(self,word):
        current_node=self.root
        length=len(word)
        for i in range (length):
            index=self.char_position(word[i])
            if current_node.children[index]==None:
                current_node.children[index]=self.getNode() 
            current_node=current_node.children[index]
            current_node.NumOfVisit=current_node.NumOfVisit+1
        current_node.IsEndOfWord=True

    def search(self,word):
        current_node=self.root
        length=len(word)
        for i in range (length):
            index=self.char_position(word[i])
            if current_node.children[index]==None:
                return 0
            else:
                current_node=current_node.children[index]
        return 1

    def prefix_search(self,prefix):
        current_node=self.root
        length=len(prefix)
        for i in range (length):
            index=self.char_position(prefix[i])
            if current_node.children[index]==None:
                return 0
            current_node=current_node.children[index]
        return current_node.NumOfVisit
                

            
                
words=["the","a","there","anaswe","any","by","their"]
dictionary=Trie()
Length=len(words)
for i in range (Length):
    dictionary.insert(words[i])
#if dictionary.search("any")==1:
    #print("Yes")
#else:
    #print("NO")
output=dictionary.prefix_search("a")
print(output)