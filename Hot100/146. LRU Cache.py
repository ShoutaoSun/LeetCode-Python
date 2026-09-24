'''
    LRU 缓存：哈希表 + 双向链表
'''

class ListNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.pre = None  # 前驱指针
        self.next = None  # 后继指针

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}  # 哈希表 key -> Node 对象

        # 创建哨兵节点
        self.head = ListNode()
        self.tail = ListNode()

        # 初识时链表为空，head 直接连 tail
        self.head.next = self.tail
        self.tail.pre = self.head

    def addToHead(self, node):  # 把一个节点插到 head 后面（标记为最近使用）
        node.pre = self.head
        node.next = self.head.next
        self.head.next.pre = node
        self.head.next = node

    def removeNode(self, node):  # 把 node 从链表里摘出来（前后接上，跳过 node）
        node.pre.next = node.next
        node.next.pre = node.pre

    def moveToHead(self, node):  # 把已有节点挪到最前面（最近使用）
        self.removeNode(node)
        self.addToHead(node)

    def removeTail(self):  # 删除最久未使用的节点（tail 前面那个），并返回它
        node = self.tail.pre
        self.removeNode(node)
        return node

    def get(self, key):
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self.moveToHead(node)
        return node.value

    def put(self, key, value):
        # case 1: key 存在
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.moveToHead(node)

        # case 2: key 不存在
        else:
            node = ListNode(key, value)
            self.cache[key] = node  # 存入哈希表
            self.addToHead(node)

            # 检查是否超容量
            if len(self.cache) > self.capacity:
                removed = self.removeTail()
                del self.cache[removed.key]
        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
