class TrieNode:
    def __init__(self):
        self.childnodes={}
        self.isword=False
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root=TrieNode()
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        currNode=self.root
        for i in word:
            if i not in currNode.childnodes:
                currNode.childnodes[i]=TrieNode()
            currNode=currNode.childnodes[i]
        currNode.isword=True
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        currNode=self.root
        for ch in word:
            if ch not in currNode.childnodes:
                return False
            currNode=currNode.childnodes[ch]
        return currNode.isword
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        currNode=self.root
        for ch in prefix:
            if ch not in currNode.childnodes:
                return False
            currNode=currNode.childnodes[ch]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
