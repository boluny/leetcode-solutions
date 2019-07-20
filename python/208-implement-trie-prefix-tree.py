# -*- coding: utf-8 -*-

class Node:
    # children looks like following:
    # {'a': node1, 'b': node2, ... 'z', node26}
    # following is actually define a class level variable not instance one!
    # foo = 32
    def __init__(self):
        self.eod = False
        self.children = {}
        

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()
        self.root.eod = True

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        curr_node = self.root
        for letter in word:
            child = Node()
            # will add node as child to to current node but need a pre check
            if not curr_node.children.get(letter):
                curr_node.children[letter] = child
                curr_node = child
            else:
                curr_node = curr_node.children[letter]
                
        # mark the node in lowest level as the end node
        # so one word is here
        curr_node.eod = True
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        curr_node = self.root
        for letter in word:
            if not curr_node.children.get(letter):
                return False
            curr_node = curr_node.children[letter]
            
        # we search to the end of the path from root to current node
        # so the search matchs string exactly
        if curr_node.eod:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        curr_node = self.root
        for letter in prefix:
            if not curr_node.children.get(letter):
                return False         
            curr_node = curr_node.children[letter]
        
        return True



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

def test_solution():
    root = Trie()
    root.insert('abc')
    assert root.search('abc') == True
    assert root.search('ab') == False

    root.insert('ab')
    assert root.search('ab') == True
    root.insert('ab')
    assert root.search('ab') == True