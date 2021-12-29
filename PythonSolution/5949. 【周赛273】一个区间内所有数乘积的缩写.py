# https://leetcode-cn.com/problems/abbreviating-the-product-of-a-range/

class Solution:
    def abbreviateProduct(self, left: int, right: int) -> str:
        M = 10 ** 10
        MOD = 10 ** 14
        
        cnt0 = 0        #末位0的个数

        #----计算后缀，并统计末位0的个数
        suf = 1
        for x in range(left, right + 1):
            suf *= x
            while suf % 10 == 0:
                cnt0 += 1
                suf //= 10
            suf %= MOD
                
                
        ok10 = False    #是否达到了10位
        
        #----计算前缀
        pref = 1
        for x in range(left, right + 1):
            pref *= x
            while pref >= 10 and pref % 10 == 0:
                pref //= 10
            if pref >= M:
                ok10 = True
            while pref >= MOD:
                pref //= 10
                
        old_pre = pref
        while pref >= 10 ** 5:
            pref //= 10
        

        if ok10 == True:
            return str(pref) + '...' + str(suf)[-5: ].rjust(5, '0') + 'e' + str(cnt0)
        return str(old_pre) + 'e' + str(cnt0)