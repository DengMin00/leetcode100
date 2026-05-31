# 法一，看了解析  55ms 击败65.1%
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums=set(nums)
        longest_streak=0
        for i in nums:
            if i-1 not in nums:
                current_num=i
                current_streak=1
               
                while current_num+1 in nums:
                   current_num+=1
                   current_streak+=1
                
                longest_streak=max(longest_streak,current_streak)
  
        return longest_streak
    
s=Solution()
nums=[100,4,200,1,3,2]
result=s.longestConsecutive(nums)
print(result)