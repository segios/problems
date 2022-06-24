from math import sqrt

class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        lst = []
        l = sqrt(n)
        for i in range(1, l+1):
            if n % i ==0:
                lst.append(i)
        
        if len(lst) <= k-1:
            return -1
        return lst[k-1]

    def kthFactor1(self, n: int, k: int) -> int:
        lst = []
        l = int(sqrt(n))
        for i in range(1, l+1):
            if n % i ==0:
                lst.append(i)
        lst.append(n)
        if len(lst) <= k-1:
            return -1
        return lst[k-1]


solution = Solution()

res = solution.kthFactor1(24, 6)
print(res)