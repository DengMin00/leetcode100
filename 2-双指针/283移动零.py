# 法一 改变了0的相对位置 不行
# class Solution(object):
#     def moveZeroes(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: None Do not return anything, modify nums in-place instead.
#         """
#         nums=sorted(nums)
#         count=0
#         for i in nums:
#             if i==0:
#                 count+=1
#         nums=nums[count:len(nums)]+nums[0:count]
#         return nums

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # slow: 指向当前可以放置非零元素的位置
        slow = 0
        
        # fast: 遍历数组
        for fast in range(len(nums)):
            if nums[fast] != 0:
                # 把非零元素放到 slow 位置
                nums[slow] = nums[fast]
                slow += 1
        
        # 把 slow 后面的位置全部填 0
        while slow < len(nums):
            nums[slow] = 0
            slow += 1    
        return nums
s=Solution()
nums = [0,1,0,3,12,0]
res=s.moveZeroes(nums)
print(res)            