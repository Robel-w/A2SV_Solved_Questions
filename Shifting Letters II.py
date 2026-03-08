class Solution:
    def shiftingLetters(self, s: str, shifts):
        n = len(s)
        diff = [0]*(n+1)

        for l,r,d in shifts:
            if d == 1:
                diff[l] += 1
                diff[r+1] -= 1
            else:
                diff[l] -= 1
                diff[r+1] += 1

        cur = 0
        res = []

        for i in range(n):
            cur += diff[i]
            shift = cur % 26
            new_char = chr((ord(s[i]) - ord('a') + shift) % 26 + ord('a'))
            res.append(new_char)

        return "".join(res)
