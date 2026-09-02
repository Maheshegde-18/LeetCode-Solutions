class Solution(object):
    def climbStairs(self, n):
        a=1
        b=2
        for _ in range(2,n+1):
            a,b=b,a+b
        return a        