#User function Template for python3
from collections import Counter
class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        countA = Counter(a)
        countB = Counter(b)
        for i in countB:
            if countB[i] > countA[i]:
                return False
        return True  
