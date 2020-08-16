class TriaNode:
    def __init__(self):
        self.children={}
        self.isword=False
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root=TriaNode()
        

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        cur=self.root
        for i in word:
            if i not in cur.children:
                cur.children[i]=TriaNode()
            cur=cur.children[i]
        cur.isword=True
        

    def search(self, word: str) -> bool:
        def dfs(node,i):
            if len(word)==i:return node.isword
            if word[i]=='.':
                for j in node.children:
                    if dfs(node.children[j],i+1):
                        return True
            if word[i] in node.children:
                    return dfs(node.children[word[i]],i+1)
            else:return False
        return dfs(self.root,0)
