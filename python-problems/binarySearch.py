# https://leetcode.com/problems/binary-search/
# 704. Binary Search
# Easy
# Binary Search
# A/B (calc mid)
# 


from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, m = 0, len(nums) -1 
        
        while l <= m :
            mid = l + ((m - l) // 2)
            #int mid = low + ((high - low) / 2);
            # mid = (low + high)  // 2 - incorrect;

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid+1
            else:
                m = mid -1 

        return  -1

solution = Solution()

#res = solution.search([9], 9)
#print(res) 

#res = solution.search([1,9], 9)
#print(res) 


res = solution.search([-1,0,3,5,9,12], 9)
print(res) 

res = solution.search([-1,0,3,5,9,12], 2)
print(res) 

