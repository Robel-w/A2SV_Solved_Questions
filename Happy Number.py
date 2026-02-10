class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        while n not in visited and n!=1:
            visited.add(n)
            summ = 0
            while n > 0:
                digit = n% 10
                summ += digit ** 2
                n //= 10
            n = summ
        return n==1 
