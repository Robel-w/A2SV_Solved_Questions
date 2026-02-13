class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        row , col = len(img) , len(img[0])
        res = [[0]*col for _ in range(row)]

        for i in range(row):
            for j in range(col):
                curr = 0
                k = 0
                # up
                if i > 0 :
                    curr += img[i-1][j]
                    k += 1
                # Down
                if i < row - 1:
                    curr += img[i+1][j]
                    k += 1
                # Left
                if j - 1 >= 0 :
                    curr += img[i][j-1]
                    k += 1
                # Right
                if j + 1 < col :
                    curr += img[i][j+1]
                    k += 1
                # Left upper diagonal
                if i - 1 >=0 and j-1 >= 0:
                    curr += img[i-1][j-1]
                    k += 1
                # Left bottom diagonal
                if i + 1 < row and j-1 >= 0 :
                    curr += img[i+1][j-1]
                    k += 1
                # Right upper diagonal
                if i -1 >= 0 and j + 1 < col : 
                    curr += img[i-1][j+1]
                    k += 1
                # Right bottom diagonal
                if i + 1 < row and j + 1 < col :
                    curr += img[i+1][j+1]
                    k += 1
                curr += img[i][j]
                k += 1
                res[i][j] = curr // k
        return res
