#
# @lc app=leetcode.cn id=287 lang=python3
#
# [287] 寻找重复数

# https://leetcode-cn.com/problems/find-the-duplicate-number/description/

# algorithms
# Medium (66.39%)
# Likes:    1348
# Dislikes: 0
# Total Accepted:    168.6K
# Total Submissions: 254.1K
# Testcase Example:  '[1,3,4,2,2]'

# 给定一个包含 n + 1 个整数的数组 nums ，其数字都在 1 到 n 之间（包括 1 和 n），可知至少存在一个重复的整数。

# 假设 nums 只有 一个重复的整数 ，找出 这个重复的数 。

# 你设计的解决方案必须不修改数组 nums 且只用常量级 O(1) 的额外空间。



# 示例 1：


# 输入：nums = [1,3,4,2,2]
# 输出：2


# 示例 2：


# 输入：nums = [3,1,3,4,2]
# 输出：3


# 示例 3：


# 输入：nums = [1,1]
# 输出：1


# 示例 4：


# 输入：nums = [1,1,2]
# 输出：1




# 提示：


# 1 
# nums.length == n + 1
# 1 
# nums 中 只有一个整数 出现 两次或多次 ，其余整数均只出现 一次
# 
# 
# 
# 
# 进阶：
# 
# 
# 如何证明 nums 中至少存在一个重复的数字?
# 你可以设计一个线性级时间复杂度 O(n) 的解决方案吗？
# 
# 
#

# @lc code=start
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # 边界
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow = 0
        while fast != slow:
            slow, fast = nums[slow], nums[fast]
        return slow

# @lc code=end

