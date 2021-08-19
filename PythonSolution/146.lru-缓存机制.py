#
# @lc app=leetcode.cn id=146 lang=python3
#
# [146] LRU缓存机制
#
# https://leetcode-cn.com/problems/lru-cache/description/
#
# algorithms
# Medium (44.89%)
# Likes:    382
# Dislikes: 0
# Total Accepted:    30.1K
# Total Submissions: 66.9K
# Testcase Example:  '["LRUCache","put","put","get","put","get","put","get","get","get"]\n' +
  '[[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]'
#
# 运用你所掌握的数据结构，设计和实现一个  LRU (最近最少使用) 缓存机制。它应该支持以下操作： 获取数据 get 和 写入数据 put 。
# 
# 获取数据 get(key) - 如果密钥 (key) 存在于缓存中，则获取密钥的值（总是正数），否则返回 -1。
# 写入数据 put(key, value) -
# 如果密钥不存在，则写入其数据值。当缓存容量达到上限时，它应该在写入新数据之前删除最近最少使用的数据值，从而为新的数据值留出空间。
# 
# 进阶:
# 
# 你是否可以在 O(1) 时间复杂度内完成这两种操作？
# 
# 示例:
# 
# LRUCache cache = new LRUCache( 2 /* 缓存容量 */ );
# 
# cache.put(1, 1);
# cache.put(2, 2);
# cache.get(1);       // 返回  1
# cache.put(3, 3);    // 该操作会使得密钥 2 作废
# cache.get(2);       // 返回 -1 (未找到)
# cache.put(4, 4);    // 该操作会使得密钥 1 作废
# cache.get(1);       // 返回 -1 (未找到)
# cache.get(3);       // 返回  3
# cache.get(4);       // 返回  4
# 
# 
#

# @lc code=start
# python 入参可以为0
class DlinkedNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.pre = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = dict()
        self.head = DlinkedNode()
        self.tail = DlinkedNode()
        self.tail.pre = self.head
        self.head.next = self.tail
        self.size = 0
        self.capacity = capacity

    def get(self, key: int) -> int:
        # 有的话返回，置顶
        if key not in self.cache:
            return -1 
        node = self.cache[key]
        self.moveToTop(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            node = DlinkedNode(key, value)
            self.cache[node.key] = node
            self.addToHead(node)
            self.size += 1
            if self.size > self.capacity:
                removed = self.removeTail()
                self.cache.pop(removed.key)
                self.size -=1
        else:
            node = self.cache[key]
            node.value = value
            self.moveToTop(node)


    def moveToTop(self, node: DlinkedNode):
        self.removeNode(node)
        self.addToHead(node)

    def removeNode(self, node: DlinkedNode):
        node.pre.next = node.next
        node.next.pre = node.pre

    def addToHead(self, node: DlinkedNode):
        node.pre = self.head
        node.next = self.head.next
        self.head.next.pre = node
        self.head.next = node

    def removeTail(self):
        node = self.tail.pre
        self.removeNode(node)
        return node
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

