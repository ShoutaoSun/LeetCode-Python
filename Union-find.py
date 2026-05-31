'''
    并查集 - 算法模板
'''

class UnionFind:
    def __init__(self, n):
        # 初始化，每个元素的父节点指向自己
        self.father = [i for i in range(n)]

    # 寻找根结点（使用剪枝策略）
    def find(self, u):
        if u == self.father[u]:
            return u
        self.father[u] = self.find(self.father[u])  # 路径压缩
        return self.father[u]

    # 添加节点
    def join(self, a, b):
        # 先判断两个元素是否已经属于同一个集合
        a = self.find(a)
        b = self.find(b)
        if a == b:
            return 
        self.father[a] = b

    # 判断两个元素是否属于同一个集合
    def is_Same(self, a, b):
        return self.find(a) == self.find(b)
    
if __name__ == "__main__":
    n = 5
    uf = UnionFind(n)

    # 添加元素
    uf.join(1, 2)
    uf.join(2, 3)

    # 判断是否属于同一集合
    print(uf.is_Same(1, 2))
    print(uf.is_Same(0, 1))