class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        row = len(image)
        col = len(image[0])
        for i in range(row):
            for j in range((col + 1) // 2):
                image[i][j], image[i][col-1-j] = image[i][col-1-j] , image[i][j]
                 
        for i in range(row):
            for j in range(col):
                if image[i][j] == 1:
                    image[i][j] = 0
                else:
                    image[i][j] = 1    
        return image            

        
