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

# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         def partition(nums, left, right):
#             pivot = nums[left]#初始化一个待比较数据
#             i,j = left, right
#             while(i < j):
#                 while(i<j and nums[j]>=pivot): #从后往前查找，直到找到一个比pivot更小的数
#                     j-=1
#                 nums[i] = nums[j] #将更小的数放入左边
#                 while(i<j and nums[i]<=pivot): #从前往后找，直到找到一个比pivot更大的数
#                     i+=1
#                 nums[j] = nums[i] #将更大的数放入右边
#             #循环结束，i与j相等
#             nums[i] = pivot #待比较数据放入最终位置 
#             return i #返回待比较数据最终位置
        
#         def topk_split(nums, k, left, right):
#     #寻找到第k个数停止递归，使得nums数组中index左边是前k个小的数，index右边是后面n-k个大的数
#             if (left<right):
#                 index = partition(nums, left, right)
#                 if index==k:
#                     return 
#                 elif index < k:
#                     topk_split(nums, k, index+1, right)
#                 else:
#                     topk_split(nums, k, left, index-1)
#         def topk_larges(nums, k):
#     #parttion是按从小到大划分的，如果让index左边为前n-k个小的数，则index右边为前k个大的数
#             topk_split(nums, len(nums)-k, 0, len(nums)-1) #把k换成len(nums)-k
#             return nums[len(nums)-k:] 
#         def topk_large(nums, k):
#     #parttion是按从小到大划分的，如果让index左边为前n-k个小的数，则index右边为前k个大的数
#            topk_split(nums, len(nums)-k, 0, len(nums)-1) #把k换成len(nums)-k
#            return nums[len(nums)-k] 
#
#        return topk_large(nums, k)
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

