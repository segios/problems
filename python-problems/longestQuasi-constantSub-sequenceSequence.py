# https://stackoverflow.com/questions/49593686/find-longest-quasi-constant-sub-sequence-of-a-sequence
# 
# 
# 
# 
# https://github.com/ufoscout/HackerRank_Java/tree/master/src/test/java/ufo/codility/toptal

from typing import List

class Solution1:
    def longestQCsubSequence(self, nums: List[int]) -> int:

        s = sorted(nums)

        maxLen = 1
        currLen = 1
        minNum = s[0]
        maxNum = s[0]
        maxNumIdx = -1
        for i in range( 1, len(s)): 
            if s[i] - minNum <= 1:
               currLen = currLen + 1
               if s[i] > minNum and maxNumIdx == -1:
                  maxNum = minNum
                  maxNumIdx = i
            else:
                maxLen = max(maxLen, currLen) 
                if maxNumIdx == -1:
                    currLen = 1
                    minNum = s[i]
                    maxNum = s[i]
                else:
                    maxNum = max(s[maxNumIdx], s[i])
                    if s[i] - s[maxNumIdx] == 1:
                        currLen = i - maxNumIdx + 1
                        minNum = s[maxNumIdx]
                        maxNumIdx = i
                    else: 
                        currLen = 1
                        minNum = s[i]
                        maxNumIdx = -1
                

        maxLen = max(maxLen, currLen) 

        return maxLen

class Solution:
    def longestQCsubSequence(self, nums: List[int]) -> int:
        dict = {}
        for i in range( 1, len(nums)): 
            if nums[i] in dict:
                dict[nums[i]] = dict[nums[i]]+1
            else :
                dict[nums[i]] = 1
            if nums[i]+1 in dict:
                dict[nums[i]+1] = dict[nums[i]+1]+1
            else :
                dict[nums[i]+1] = 1
            if nums[i]-1 in dict:
                dict[nums[i]-1] = dict[nums[i]-1]+1
            else :
                dict[nums[i]-1] = 1
        
        res = max(dict, key=lambda key: dict[key])
        return dict[res]
    
from collections import Counter

def solution(seq):
    if not seq:     # special case for empty input sequence
        return 0
    counts = Counter(seq)
    return max(counts[x] + counts[x+1] for x in counts)

from collections import defaultdict

def longestQuasiConstantSubseqLength(seq):
  d = defaultdict(int)
  for s in seq:
    d[s] += 1
    d[s+1] += 1
  return max(d.values() or [0])

#solution = Solution()
seq = [6,10,6,9,7,8]
#res = solution.longestQCsubSequence(seq)
res = solution(seq)
res = longestQuasiConstantSubseqLength(seq)
print(res)          

seq = [1,7,6,2,6,4]
#res = solution.longestQCsubSequence(seq)
res = solution(seq)
res = longestQuasiConstantSubseqLength(seq)
print(res)          
