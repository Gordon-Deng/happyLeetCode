/*
 * @lc app=leetcode.cn id=42 lang=java
 *
 * [42] 接雨水
 *
 * https://leetcode-cn.com/problems/trapping-rain-water/description/
 *
 * algorithms
 * Hard (47.85%)
 * Likes:    858
 * Dislikes: 0
 * Total Accepted:    53.4K
 * Total Submissions: 110K
 * Testcase Example:  '[0,1,0,2,1,0,1,3,2,1,2,1]'
 *
 * 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
 * 
 * 
 * 
 * 上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 感谢
 * Marcos 贡献此图。
 * 
 * 示例:
 * 
 * 输入: [0,1,0,2,1,0,1,3,2,1,2,1]
 * 输出: 6
 * 
 */

// @lc code=start

// T:O(n) S:O(1)
class Solution {
    public int trap(int[] height) {
        /*
        使用两个指针，一个 left_max ，一个 right_max

        这个双指针是怎么个使用法呢？
        首先每次循环开始，先获取 left 的左边 [0, left - 1] 最高柱子高度 和 right 右边 [right + 1, len - 1] 最高柱子高度（都不包括 left 和 right 本身）
        当 left_max < right_max 时，那么就说明对于 left 右边一定有比 left_max 更高的柱子，那么只需要判断 left 左边 最高柱子 left_max 是否比 left 柱子高就行了，如果是，那么就能装水
        当 left_max >= right_max 时，那么就说明对于 right 左边一定有比 right_max 更高或者相同高度的柱子，那么只需要判断 right 右边最高柱子 right_max 是否比 right 柱子高就行了
        其实就是保证哪边稳定有高柱子就查看哪边
        
        为什么可以隔这么远进行判断？
        比如 对于 left 柱子，如果 left_max 比 left 高，那么如果 right_max 比 left_max 高，那么就跟上面说的 left 右边一定存在比 left 高的柱子，那么 left 柱能装水，
        就算 right_max 对于 left 右边来说不是最高的柱子也无所谓，因为如果不是最高的柱子，那么同样存在另一个比 left 高的柱子，那么 left 同样也能装水，且装水量同样是 left_max - left

        当 left_max < right_max 时，那么当前柱 left 装水量就是直接 left_max - height[left];
        当 left_max >= right_max 时，那么当前柱 right 装水量就是直接， right_max - height[right]
        */
        int left_max = 0;
        int right_max = 0;
        int res = 0;
        int left = 1;
        int right = height.length - 2;
        /*
        为什么需要 left == right?
        比如 [0,1,0,2,1,0,1,3,2,1,2,1]
                      1
              1       1 1   1
        0 1 0 1 1 0 1 1 1 1 1 1
                    ↑
                  right
                    ↑
                   left
        当 right_max == 3 时，那么就说明 right 已经到了 3 柱子的下一个 了，即 height[right] == 1
        这时看左边，左边已经没有比 3 更高的了，因此 left 会一直 left++，直到发现 和 right 重合，
        而这时 left_max == 2，而 right_max == 3，同时 height[left(right)] == 1，但这根柱子还没有进行判断并且是可以装水的，如果 left == right 就退出循环，那么就会漏掉这柱子的装水量
        */
        while (left <= right) {
            left_max = Math.max(left_max, height[left - 1]);
            right_max = Math.max(right_max, height[right + 1]);
            if (left_max < right_max) {
                if (left_max > height[left]) {
                    res += left_max - height[left];
                }
                left++;
            } else {
                if (right_max > height[right]) {
                    res += right_max - height[right];
                }
                right--;
            }
        }
        return res;
    }
}
// @lc code=end

