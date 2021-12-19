# https://leetcode-cn.com/problems/find-first-palindromic-string-in-the-array/

class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        # 判断字符串是否回文
        def isPalindrome(word: str) -> bool:
            n = len(word)
            l, r = 0, n - 1
            while l < r:
                if word[l] != word[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        # 顺序遍历字符串数组，如果遇到回文字符串则返回，未遇到则返回空字符串
        for word in words:
            if isPalindrome(word):
                return word
        return ""