#
# @lc app=leetcode.cn id=239 lang=python3
#
# [239] 滑动窗口最大值

# https://leetcode-cn.com/problems/sliding-window-maximum/description/

# algorithms
# Hard (49.58%)
# Likes:    1123
# Dislikes: 0
# Total Accepted:    177K
# Total Submissions: 356.9K
# Testcase Example:  '[1,3,-1,-3,5,3,6,7]\n3'

# 给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k
# 个数字。滑动窗口每次只向右移动一位。

# 返回滑动窗口中的最大值。



# 示例 1：


# 输入：nums = [1,3,-1,-3,5,3,6,7], k = 3
# 输出：[3,3,5,5,6,7]
# 解释：
# 滑动窗口的位置                最大值
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
# ⁠1 [3  -1  -3] 5  3  6  7       3
# ⁠1  3 [-1  -3  5] 3  6  7       5
# ⁠1  3  -1 [-3  5  3] 6  7       5
# ⁠1  3  -1  -3 [5  3  6] 7       6
# ⁠1  3  -1  -3  5 [3  6  7]      7


# 示例 2：


# 输入：nums = [1], k = 1
# 输出：[1]


# 示例 3：


# 输入：nums = [1,-1], k = 1
# 输出：[1,-1]


# 示例 4：


# 输入：nums = [9,11], k = 2
# 输出：[11]


# 示例 5：


# 输入：nums = [4,-2], k = 2
# 输出：[4]
# 
# 
# 
# 提示：
# 
# 
# 1 
# -10^4 
# 1 
# 
# 
#

# @lc code=start

# heapq.heapify(q)堆的操作
# 原理有点拗口，就是每次维护一个大顶堆，注意不要被窗口大小限制思想，这道题不用理固定堆的大小就为K，只需要看堆顶的最大值是否在当前窗口即可
# 当滑动窗口移动时，若最大值不在窗口，那就弹出去，否则一值滑动一直往堆里加元素就好了
# class Solution:
#     def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
#         n = len(nums)
#         # 注意 Python 默认的优先队列是小根堆
#         q = [(-nums[i], i) for i in range(k)]
#         heapq.heapify(q)

#         ans = [-q[0][0]]
#         for i in range(k, n):
#             heapq.heappush(q, (-nums[i], i))
#             while q[0][1] <= i - k:
#                 heapq.heappop(q)
#             ans.append(-q[0][0])
        
#         return ans

# 双端队列
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        dq = deque()
        
        for i in range(len(nums)):
            # 只要当前遍历的元素的值比队尾大，让队尾出队列，
            # 最终队列中的最小元素是大于当前元素的
            while dq and dq[-1] < nums[i]:
                dq.pop()
            # 当前遍历的元素入队列， 此时队列中的元素一定是有序的，队列头部最大
            dq.append(nums[i])
            if i >= k - 1:
                # 如果窗口即将失效（下一次循环要失效）的值与当前对列头部的值相同，那么将对头的值出队列，
                # 注意只pop一次，可能两个4，相邻同时是最大值，
                ans.append(dq[0])
                # 从队列中删除即将失效的数据
                if nums[i - k + 1] == dq[0]:
                    dq.popleft()
        return ans

# 定义一个双向链表
class LinkNode:
    def __init__(self, val=0):
        self.next = None
        self.prev = None
        self.val = val

# https://leetcode-cn.com/problems/sliding-window-maximum/solution/na-yao-wen-ti-lai-liao-ru-guo-mian-shi-g-8waf/
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1: return nums

        head = LinkNode()
        tail = LinkNode()
        head.next = tail
        tail.prev = head

        # 尾部添加节点，类似于 “append”
        def add_node_to_tail(node):
            node.next = tail
            node.prev = tail.prev
            tail.prev.next = node
            tail.prev = node

        # 删除头节点，类似于Java中的 “poll”
        def remove_node_from_head():
            head.next.next.prev = head
            head.next = head.next.next

        # 删除尾部节点，类似于 “pop()”
        def remove_node_from_tail():
            tail.prev.prev.next = tail
            tail.prev = tail.prev.prev

        # 获得尾部节点，类似于 "list[-1]”
        def get_last_node():
            node = tail.prev
            return node

        # 获得头节点，类似于 “list[0]”
        def get_first_node():
            node = head.next
            return node

        # 定义完以上函数，下面的操作与什么双端队列呀，单调栈呀类似，这里不再啰嗦
        # 但要记得链表的基本操作方法，这是基本功，这个如果不会的话，可以直接路过～
        res, n = [], len(nums)
        for i in range(0, n):
            while tail.prev.prev and nums[i] > nums[get_last_node().val]:
                remove_node_from_tail()
            add_node_to_tail(LinkNode(i))
            if get_first_node().val <= i-k:
                remove_node_from_head()
            if i + 1 >= k:
                res.append(nums[get_first_node().val])
        return res

from typing import List


class LinkNode:
    def __init__(self, val=0):
        self.prev = None
        self.next = None
        self.val = val


class Solution:
    # def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
    # 边界
    # ans = []
    # q = deque()
    # if k > len(nums):
    #     return nums

    # for i in range(len(nums)):
    #     while q and q[-1] < nums[i]:
    #         q.pop()
    #     q.append(nums[i])
    #     if 0 <= i-k+1:
    #         ans.append(q[0])
    #         if nums[i-k+1] == q[0]:
    #             q.popleft()
    # return ans
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        if k > len(nums):
            return nums
        self.head = LinkNode()
        self.tail = LinkNode()
        self.head.next = self.tail
        self.tail.prev = self.head

        for i in range(len(nums)):
            # 判空注意是tail.prev.prev
            while self.tail.prev.prev and self.get_queue_last_node().val < nums[i]:
                self.remove_node_from_tail()
            self.add_node_to_tail(LinkNode(nums[i]))
            if 0 <= i - k + 1:
                ans.append(self.get_queue_first_node().val)
                if nums[i - k + 1] == self.get_queue_first_node().val:
                    self.pop_the_leftest_node()
        return ans

    def add_node_to_tail(self, node: LinkNode):
        # self.tail.next = node
        # node.prev = self.tail
        # node.next = self.head
        # self.head.prev = node
        # self.tail = node

        node.next = self.tail
        node.prev = self.tail.prev
        self.tail.prev.next = node
        self.tail.prev = node

    def get_queue_first_node(self):
        return self.head.next

    def get_queue_last_node(self):
        return self.tail.prev

    def pop_the_leftest_node(self):
        # temp2 = self.head.next
        # self.head.next.prev = self.tail
        # self.tail.next = self.head.next
        # self.head = temp2

        self.head.next.next.prev = self.head
        self.head.next = self.head.next.next

    def remove_node_from_tail(self):
        # self.tail.prev.next = self.head
        # self.head.prev = self.tail.prev
        # self.tail = self.tail.prev

        self.tail.prev.prev.next = self.tail
        self.tail.prev = self.tail.prev.prev
# @lc code=end

