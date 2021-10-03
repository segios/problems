# https://leetcode.com/problems/permutations-ii/
# 47. Permutations II
# Medium
# Backtracking
# C
# 

import copy 
from typing import List
from collections import Counter 

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def backtrack(first = 0):
            # if all integers are used up
            used = set()
            if first == n:  
                output.append(nums[:])
            for i in range(first, n):
                # place i-th integer first 
                # in the current permutation
                if nums[i] not in used:
                    used.add(nums[i])
                    nums[first], nums[i] = nums[i], nums[first]
                    # use next integers to complete the permutations
                    backtrack(first + 1)
                    # backtrack
                    nums[first], nums[i] = nums[i], nums[first]

        n = len(nums)
        output = []
        backtrack()
        return output

class Solution2:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        results = []
        def backtrack(comb, counter):
            if len(comb) == len(nums):
                # make a deep copy of the resulting permutation,
                # since the permutation would be backtracked later.
                results.append(list(comb))
                return

            for num in counter:
                if counter[num] > 0:
                    # add this number into the current combination
                    comb.append(num)
                    counter[num] -= 1
                    # continue the exploration
                    backtrack(comb, counter)
                    # revert the choice for the next exploration
                    comb.pop()
                    counter[num] += 1

        backtrack([], Counter(nums))

        return results

class Solution1:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)

        def permute(nums):
            if len(nums) == 1:
                return [nums[:]]

            result = []

            prev = -11
            for _ in range(len(nums)):
                num = nums.pop(0)
                if num != prev:
                    perms = permute(nums)
                    for perm in perms:
                        perm.append(num)
                    result.extend(perms)        
                nums.append(num)
                prev = num
            return result
        
        return permute(nums)

class Solution3:
    def permuteUnique(self, A: List[int]) -> List[List[int]]:
        def nextp(A):
            n = len(A)
            i = n-2
            while i>=0 and A[i]>=A[i+1]:
                i-=1
            if i<0: return False
            j = n-1
            while A[j]<=A[i]: j-=1
            A[i],A[j]=A[j],A[i]
            A[i+1:] = A[:i:-1]
            return True
        A.sort()
        ret = [A.copy()]
        while nextp(A):
            ret.append(A.copy())
        return ret

class Solution4:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return nums
        nums.sort()
        permutations = [[]]
        for n in nums:
            new_permutations = []
            l = len(permutations[-1])
            for seq in permutations:
                for i in range(l, -1, -1):
                    if i < l and seq[i] == n:
                        break
                    new_permutations.append(seq[:i] + [n] + seq[i:])
            permutations = new_permutations
        return permutations

solution = Solution()

res = solution.permuteUnique([1,1,2])
print(res)    
