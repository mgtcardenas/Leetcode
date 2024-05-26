class Solution:
    def isPalindrome(self, x: int) -> bool:
        if(x >= 0):
            digits = []
            while (x > 0):
                digits.append(int(x % 10))
                x = int(x / 10)
            return digits == digits[::-1]
        return False
