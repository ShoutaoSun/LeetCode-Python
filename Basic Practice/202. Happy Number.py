'''
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

- Starting with any positive integer, replace the number by the sum of the squares of its digits.
- Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
- Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

Example:
Input: n = 19
Output: true
'''

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        record = set()

        while True:
            n = self.get_sum(n)
            if n == 1:
                return True
            
            if n in record:
                return False
            else:
                record.add(n)
        

    def get_sum(self, n):
        sum = 0
        while n:
            n, r = divmod(n, 10)
            sum += r ** 2
        return sum

# test
n = 19
print(Solution.isHappy(Solution(), n))