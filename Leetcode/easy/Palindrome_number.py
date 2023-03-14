# https://leetcode.com/problems/palindrome-number/submissions/849382082/
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        x = str(x)
        n = len(x)
        i = 0
        while i != n//2:
            if x[i] != x[-1-i]:
                return False
            i += 1
        return True


# Best code
class Solution:
    def isPalindrome(self, x: int) -> bool:
        a = str(x)
        b = a[::-1]
            return a == b
