"""

 请你设计并实现一个满足 
 LRU (最近最少使用) 缓存 约束的数据结构。
 

 
 实现 
 LRUCache 类：
 

 
 
 
 LRUCache(int capacity) 以 正整数 作为容量 capacity 初始化 LRU 缓存 
 int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。 
 void put(int key, int value) 如果关键字 key 已经存在，则变更其数据值 value ；如果不存在，则向缓存中插入该组 key-
value 。如果插入操作导致关键字数量超过 capacity ，则应该 逐出 最久未使用的关键字。 
 
 
 

 函数 get 和 put 必须以 O(1) 的平均时间复杂度运行。 

 

 示例： 

 
输入
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
输出
[null, null, null, 1, null, -1, null, -1, 3, 4]

解释
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // 缓存是 {1=1}
lRUCache.put(2, 2); // 缓存是 {1=1, 2=2}
lRUCache.get(1);    // 返回 1
lRUCache.put(3, 3); // 该操作会使得关键字 2 作废，缓存是 {1=1, 3=3}
lRUCache.get(2);    // 返回 -1 (未找到)
lRUCache.put(4, 4); // 该操作会使得关键字 1 作废，缓存是 {4=4, 3=3}
lRUCache.get(1);    // 返回 -1 (未找到)
lRUCache.get(3);    // 返回 3
lRUCache.get(4);    // 返回 4
 

 

 提示： 

 
 1 <= capacity <= 3000 
 0 <= key <= 10000 
 0 <= value <= 10⁵ 
 最多调用 2 * 10⁵ 次 get 和 put 
 

 Related Topics 设计 哈希表 链表 双向链表 👍 2613 👎 0

"""


# leetcode submit region begin(Prohibit modification and deletion)
class DLinkedNode:

    def __init__(self, key: int = 0, value: int = 0):
        self.key = key
        self.value = value
        self.pre = None
        self.nxt = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.cache = dict()
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        self.head.nxt = self.tail
        self.tail.pre = self.head

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.moveToHead(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            node = DLinkedNode(key, value)
            self.cache[key] = node
            self.insertToHead(node)
            self.size += 1
            if self.size > self.capacity:
                removed = self.removeTail()
                del self.cache[removed.key]
                self.size -= 1
        else:
            node = self.cache[key]
            node.value = value
            self.moveToHead(node)

    def moveToHead(self, node: DLinkedNode) -> None:
        self.remove(node)
        self.insertToHead(node)

    def removeTail(self) -> DLinkedNode:
        node = self.tail.pre
        self.remove(node)
        return node

    def insertToHead(self, node: DLinkedNode) -> None:
        temp = self.head.nxt
        self.head.nxt = node
        node.pre = self.head
        node.nxt = temp
        temp.pre = node

    def remove(self, node: DLinkedNode) -> None:
        node.pre.nxt = node.nxt
        node.nxt.pre = node.pre

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# leetcode submit region end(Prohibit modification and deletion)
