# 法一 3771ms 击败5%
# class Solution(object):
#     def groupAnagrams(self, strs):
#         """
#         :type strs: List[str]
#         :rtype: List[List[str]]
#         """
#         temp=[]
#         for w in strs:
#             s=''.join(sorted(w))
#             temp.append(s)
    

#         all=[]
#         samp=[]
        
#         for i in set(temp):
#             samp=[]
#             for j,k in enumerate(temp):
#                 if i==k:
#                     samp.append(strs[j])
#             all.append(samp)
#         return all


# 法二  19ms 击败83.5% 内存15.53 击败99.37%       
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
        
        result = {}  # 字典：键是质数乘积，值是单词列表
        
        for word in strs:
            # 计算每个单词的质数乘积（作为唯一标识）
            product = 1
            for char in word:
                index = ord(char) - ord('a')  # 获取字母位置（0-25）
                product *= primes[index]      # 乘以对应的质数
            
            # 将单词添加到对应的组中
            if product in result:
                result[product].append(word)
            else:
                result[product] = [word]
        
        # 返回所有分组
        return list(result.values())         

s=Solution()

strs= ["eat", "tea", "tan", "ate", "nat", "bat"]
