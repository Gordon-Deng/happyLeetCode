#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] 数组中的第K个最大元素
#
# https://leetcode-cn.com/problems/kth-largest-element-in-an-array/description/
#
# algorithms
# Medium (60.24%)
# Likes:    345
# Dislikes: 0
# Total Accepted:    72.8K
# Total Submissions: 120.1K
# Testcase Example:  '[3,2,1,5,6,4]\n2'
#
# 在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
# 
# 示例 1:
# 
# 输入: [3,2,1,5,6,4] 和 k = 2
# 输出: 5
# 
# 
# 示例 2:
# 
# 输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
# 输出: 4
# 
# 说明: 
# 
# 你可以假设 k 总是有效的，且 1 ≤ k ≤ 数组的长度。
# 
#

# @lc code=start
# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         heap = list()
#         for num in nums:
#             heapq.heappush(heap, num)
#             if len(heap) > k:
#                 heapq.heappop(heap)
#         return heap[0]

# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         heap = Heap(k + 1)
#         for num in nums:
#             if not heap.push(num):
#                 heap.pop()
#                 heap.push(num)
#         if heap.size == k + 1:
#             heap.pop()
#         return heap.peek()
        
# class Heap:
#     def __init__(self, length):
#         self.heap = [0] * (length + 1)
#         self.size = 0
    
#     def push(self, val):
#         if self.size == len(self.heap) - 1:
#             return False
#         self.size += 1
#         self.heap[self.size] = val
#         self.shift_up(self.size)
#         return True
    
#     def pop(self):
#         val = self.heap[1]
#         self.heap[1] = self.heap[self.size]
#         self.heap[self.size] = 0
#         self.size -= 1
#         self.shift_down(1)
#         return val
    
#     def peek(self):
#         return self.heap[1]
    
#     def shift_up(self, i):
#         val = self.heap[i]
#         while i >> 1 > 0:
#             parent = i >> 1
#             if val < self.heap[parent]:
#                 self.heap[i] = self.heap[parent]
#                 i = parent
#             else:
#                 break
#         self.heap[i] = val
    
#     def shift_down(self, i):
#         val = self.heap[i]
#         while i << 1 <= self.size:
#             child = i << 1
#             if child != self.size and self.heap[child + 1] < self.heap[child]:
#                 child += 1
#             if val > self.heap[child]:
#                 self.heap[i] = self.heap[child]
#                 i = child
#             else:
#                 break
#         self.heap[i] = val
import random

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def findTopKth(low, high):
            pivot = random.randint(low, high)
            nums[low], nums[pivot] = nums[pivot], nums[low]
            base = nums[low]
            i = low
            j = low + 1
            while j <= high:
                if nums[j] > base:
                    nums[i + 1], nums[j] = nums[j], nums[i + 1]
                    i += 1
                j += 1
            nums[low], nums[i] = nums[i], nums[low]
            if i == k - 1:
                return nums[i]
            elif i > k - 1:
                return findTopKth(low, i - 1)
            else:
                return findTopKth(i + 1, high)
        return findTopKth(0, len(nums) - 1)

# https://leetcode-cn.com/problems/kth-largest-element-in-an-array/solution/ji-yu-kuai-pai-de-suo-you-topkwen-ti-jia-ylsd/
# @lc code=end

