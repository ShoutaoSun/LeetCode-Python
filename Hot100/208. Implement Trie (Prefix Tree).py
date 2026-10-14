'''
    实现 Trie (前缀树)
'''

class Node:
    __slots__ = 'son', 'end'  # 限制属性，省内存

    def __init__(self):
        self.son = [None] * 26  # 26 个字母
        self.end = False  # 是否为某个单词的结尾

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        cur = self.root
        for c in word:
            c = ord(c) - ord('a')  # 把字母转成 0~25 的下标
            if cur.son[c] is None:
                cur.son[c] = Node()
            cur = cur.son[c]
        cur.end = True

    def find(self, word):
        cur = self.root
        for c in word:
            c = ord(c) - ord('a')
            if cur.son[c] is None:
                return 0
            cur = cur.son[c]
        return 2 if cur.end else 1  # 2（完全匹配） 1（前缀匹配）

    def search(self, word):
        return self.find(word) == 2

    def startsWith(self, prefix):
        return self.find(prefix) != 0    


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)