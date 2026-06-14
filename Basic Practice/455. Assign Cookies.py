'''
Assume you are an awesome parent and want to give your children some cookies. But, you should give each child at most one cookie.
Each child i has a greed factor g[i], which is the minimum size of a cookie that the child will be content with; and each cookie j has a size s[j]. If s[j] >= g[i], we can assign the cookie j to the child i, and the child i will be content. Your goal is to maximize the number of your content children and output the maximum number.

Example:
Input: g = [1,2,3], s = [1,1]
Output: 1
'''

class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        index, cnt = len(s)-1, 0
        g.sort()
        s.sort()
        for i in range(len(g)-1, -1, -1):
            if index > -1 and s[index] >= g[i]:
                cnt += 1
                index -= 1

        return cnt

# test
g = [1, 2, 3]
s = [1, 2]
print(Solution.findContentChildren(Solution(), g, s))