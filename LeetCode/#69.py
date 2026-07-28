class Solution:
    def mySqrt(self, x: int) -> int:
        op = 0
        for i in range(x):
            if i <= 1:
                op += i
            else:
                if (i*i) <= x:
                    op *= i
        return op