class Solution:
    def countGoodNumbers(self, n: int) -> int:
        def power(x, n):
            if n == 0:
                return 1
            
            half = power(x, n // 2)
            
            if n % 2 == 0:
                return (half * half) %(10**9 + 7)
            else:
                return (x * half * half) % (10**9 + 7)
        
        even_pos = (n + 1) // 2
        odd_pos = n // 2
        
        return (power(5, even_pos) * power(4, odd_pos)) % (10**9 + 7)
