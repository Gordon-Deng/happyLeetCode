/*
 * @lc app=leetcode.cn id=4 lang=java
 *
 * [4] 寻找两个有序数组的中位数
 *
 * https://leetcode-cn.com/problems/median-of-two-sorted-arrays/description/
 *
 * algorithms
 * Hard (36.51%)
 * Likes:    2002
 * Dislikes: 0
 * Total Accepted:    130.6K
 * Total Submissions: 357.6K
 * Testcase Example:  '[1,3]\n[2]'
 *
 * 给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。
 * 
 * 请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。
 * 
 * 你可以假设 nums1 和 nums2 不会同时为空。
 * 
 * 示例 1:
 * 
 * nums1 = [1, 3]
 * nums2 = [2]
 * 
 * 则中位数是 2.0
 * 
 * 
 * 示例 2:
 * 
 * nums1 = [1, 2]
 * nums2 = [3, 4]
 * 
 * 则中位数是 (2 + 3)/2 = 2.5
 * 
 * 
 */

// @lc code=start

// T:O(log(min(m,n))) S:O(1)
// 首先，查找的区间是 [0, m][0,m]。
// 而该区间的长度在每次循环之后都会减少为原来的一半。
// 所以，我们只需要执行 \log(m)log(m) 次循环。由于我们在每次循环中进行常量次数的操作，所以时间复杂度为 O\big(\log(m)\big)O(log(m))。
// 由于 m \leq nm≤n，所以时间复杂度是 O\big(\log\big(\text{min}(m,n)\big)\big)O(log(min(m,n)))
/*
* 1.首先，让我们在任一位置 i 将 A(长度为m) 划分成两个部分：
*            leftA            |                rightA
*   A[0],A[1],...      A[i-1] |  A[i],A[i+1],...A[m - 1]
*
* 由于A有m个元素，所以有m + 1中划分方式(i = 0 ~ m)
*
* 我们知道len(leftA) = i, len(rightA) = m - i;
* 注意：当i = 0时，leftA是空集，而当i = m时，rightA为空集。
*
* 2.采用同样的方式，将B也划分为两部分：
*            leftB            |                rightB
*   B[0],B[1],...      B[j-1] |   B[j],B[j+1],...B[n - 1]
*  我们知道len(leftA) = j, len(rightA) = n - j;
*
*  将leftA和leftB放入一个集合，将rightA和rightB放入一个集合。再把这两个集合分别命名为leftPart和rightPart。
*
*            leftPart         |                rightPart
*   A[0],A[1],...      A[i-1] |  A[i],A[i+1],...A[m - 1]
*   B[0],B[1],...      B[j-1] |  B[j],B[j+1],...B[n - 1]
*
*   如果我们可以确认：
*   1.len(leftPart) = len(rightPart); =====> 该条件在m+n为奇数时，该推理不成立
*   2.max(leftPart) <= min(rightPart);
*
*   median = (max(leftPart) + min(rightPart)) / 2;  目标结果
*
*   要确保这两个条件满足：
*   1.i + j = m - i + n - j(或m - i + n - j + 1)  如果n >= m。只需要使i = 0 ~ m，j = (m+n+1)/2-i =====> 该条件在m+n为奇数/偶数时，该推理都成立
*   2.B[j] >= A[i-1] 并且 A[i] >= B[j-1]
*
*   注意:
*   1.临界条件：i=0,j=0,i=m,j=n。需要考虑
*   2.为什么n >= m ? 由于0 <= i <= m且j = (m+n+1)/2-i,必须确保j不能为负数。
*
*   按照以下步骤进行二叉树搜索
*   1.设imin = 0,imax = m，然后开始在[imin,imax]中进行搜索
*   2.令i = (imin+imax) / 2, j = (m+n+1)/2-i
*   3.现在我们有len(leftPart) = len(rightPart)。而我们只会遇到三种情况：
*
*      ①.B[j] >= A[i-1] 并且 A[i] >= B[j-1]  满足条件
*      ②.B[j-1] > A[i]。此时应该把i增大。 即imin = i + 1;
*      ③.A[i-1] > B[j]。此时应该把i减小。 即imax = i - 1;
*
* */
// https://leetcode-cn.com/problems/median-of-two-sorted-arrays/solution/xiang-xi-tong-su-de-si-lu-fen-xi-duo-jie-fa-by-w-2/
class Solution {
    // public double findMedianSortedArrays(int[] A, int[] B) {
    // 二分太难理解
    // int m = A.length;
    // int n = B.length;
    // if (m > n) {
    // return findMedianSortedArrays(B,A); // 保证 m <= n
    // }
    // int iMin = 0, iMax = m;
    // while (iMin <= iMax) {
    // int i = (iMin + iMax) / 2;
    // int j = (m + n + 1) / 2 - i;
    // if (j != 0 && i != m && B[j-1] > A[i]){ // i 需要增大
    // iMin = i + 1;
    // }
    // else if (i != 0 && j != n && A[i-1] > B[j]) { // i 需要减小
    // iMax = i - 1;
    // }
    // else { // 达到要求，并且将边界条件列出来单独考虑
    // int maxLeft = 0;
    // if (i == 0) { maxLeft = B[j-1]; }
    // else if (j == 0) { maxLeft = A[i-1]; }
    // else { maxLeft = Math.max(A[i-1], B[j-1]); }
    // if ( (m + n) % 2 == 1 ) { return maxLeft; } // 奇数的话不需要考虑右半部分

    // int minRight = 0;
    // if (i == m) { minRight = B[j]; }
    // else if (j == n) { minRight = A[i]; }
    // else { minRight = Math.min(B[j], A[i]); }

    // return (maxLeft + minRight) / 2.0; //如果是偶数的话返回结果
    // }
    // }
    // return 0.0;
    // }

    // 还是topk法好
    // T:O(log(m+n)) S:O(1)
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int n = nums1.length;
        int m = nums2.length;
        int left = (n + m + 1) / 2;
        int right = (n + m + 2) / 2;
        // 将偶数和奇数的情况合并，如果是奇数，会求两次同样的 k 。
        return (getKth(nums1, 0, n - 1, nums2, 0, m - 1, left) + getKth(nums1, 0, n - 1, nums2, 0, m - 1, right)) * 0.5;
    }

    private int getKth(int[] nums1, int start1, int end1, int[] nums2, int start2, int end2, int k) {
        int len1 = end1 - start1 + 1;
        int len2 = end2 - start2 + 1;
        // 让 len1 的长度小于 len2，这样就能保证如果有数组空了，一定是 len1
        if (len1 > len2)
            return getKth(nums2, start2, end2, nums1, start1, end1, k);
        if (len1 == 0)
            return nums2[start2 + k - 1];

        if (k == 1)
            return Math.min(nums1[start1], nums2[start2]);

        int i = start1 + Math.min(len1, k / 2) - 1;
        int j = start2 + Math.min(len2, k / 2) - 1;

        if (nums1[i] > nums2[j]) {
            return getKth(nums1, start1, end1, nums2, j + 1, end2, k - (j - start2 + 1));
        } else {
            return getKth(nums1, i + 1, end1, nums2, start2, end2, k - (i - start1 + 1));
        }
    }
}
// @lc code=end
