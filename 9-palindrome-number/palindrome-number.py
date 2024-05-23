class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        y=""
        for i in x[::-1]:
            y=y+i
        if y==x:
            return True
