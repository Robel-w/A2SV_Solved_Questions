class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or x != 0 and x % 10 == 0:
            return False
        rs = 0
        while rs< x:
            rs = rs*10
            rs += x % 10
            x //= 10
        return rs == x  or x == rs // 10   
