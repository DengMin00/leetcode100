# 法一 超出时间限制 34/98
# class Solution(object):
#     def numSubarrayProductLessThanK(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: int
#         """
#         temp1 = []
        
#         # 枚举窗口大小从 1 到 len(nums)
#         for windowSize in range(1, len(nums) + 1):
#             # 枚举窗口起始位置
#             for start in range(len(nums) - windowSize + 1):
#                 temp2 = []
#                 multi = 1
#                 # 逐个取元素
#                 for i in range(windowSize):
#                     current = nums[start + i]  # 修复：从 start 开始，不是 windowSize
#                     temp2.append(current)
#                     multi *= current
                
#                 # 修复：判断整个窗口的乘积，不是单个元素
#                 if multi < k:
#                     temp1.append(temp2)
        
#         return len(temp1)

# 法二 超出时间限制 76/98
# class Solution(object):
#     def numSubarrayProductLessThanK(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: int
#         """
#         count=0
#         for i in range(len(nums)):
#             multi=1
#             for j in range (i,len(nums)):
#                 multi*=nums[j]
#                 if multi<k:
#                     count+=1
#                 else:
#                     break
#         return count

class Solution:
    def numSubarrayProductLessThanK(self, nums, k) :
        if k <= 1:
            return 0
        ans = left = 0
        prod = 1
        for right, x in enumerate(nums):
            prod *= x
            while prod >= k:  # 不满足要求
                prod //= nums[left]
                left += 1  # 缩小窗口
            # 对于固定的 right，有 right-left+1 个合法的左端点
            ans += right - left + 1
        return ans


                     
s=Solution()
nums=[10,5,2,6]
k=100
r=s.numSubarrayProductLessThanK(nums,k)                     
print(r)