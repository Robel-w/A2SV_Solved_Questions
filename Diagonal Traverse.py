class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        mp={}
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if i + j not in mp:
                    mp[i+j] = [matrix[i][j]]
                else:
                    mp[i+j].append(matrix[i][j])
        ans= []
        for entry in mp.items():
            if entry[0] % 2 == 0:
                [ans.append(x) for x in entry[1][::-1]]
            else:
                [ans.append(x) for x in entry[1]]
        return ans
                
            






