# 列表 in 是"逐个看"，字典 in 是"直接算"。
# 这个技巧叫 "哈希表" 或 "空间换时间" —— 多花一点内存存索引，换取速度的巨大提升。

# 法一 679ms 击败35.72%
# 最坏的情况要遍历整个数组
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            j=target-nums[i]
            if j in nums and nums.index(j)!=i:
                return [i,nums.index(j)]
        return    
            

# 法二
# enumerate 是 Python 的一个内置函数，作用很简单：同时拿到列表的"索引"和"值"，不用自己数。
# enumerate() 不转换字典，它生成的是带索引的元组序列。
#  seen[x]是在取索引，这个字典值是索引

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen={}
        for j,x in enumerate(nums):
            if target-x in seen:
                return [seen[target-x],j]
            seen[x]=j
 
            
s=Solution()

nums = [2, 7, 11, 15]
target = 9

result=s.twoSum(nums,target)
print(result)        