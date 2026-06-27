'''
    哈希 - 字母异位词分组
'''

class Solution:
    def groupAnagrams(self, strs):
        hash_table = {}
        result = []

        for s in strs:
            str_list = sorted(s)  # 字符串排序后得到的是一个列表
            sorted_str = ''.join(str_list)  # 重新组合成字符串

            if sorted_str in hash_table:
                hash_table[sorted_str].append(s)
            else:
                hash_table[sorted_str] = [s]
        
        for _, value in hash_table.items():
            result.append(value)

        return result

# test
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(Solution.groupAnagrams(Solution, strs))