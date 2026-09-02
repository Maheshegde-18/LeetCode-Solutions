class Solution(object):
    def fib(self, n):
        a=0
        b=1
        for _ in range(n):
            a,b=b,a+b
        return a

        