class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        mapp = {}
        res = []
        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i] == list2[j]:
                    mapp[list1[i]] = i + j
        minn = float('inf')            
        for a, b in mapp.items():
            minn = min(minn, b)
        for a, b in mapp.items():
            if b == minn:
                res.append(a)
        return res        
        # minn = float('inf')
        # res = []
        # for i in range(len(list1)):
        #     if list1[i] in list2:
        #         j = list2.index(list1[i])
        #         if i + j < minn:
        #             minn = i+j
        #             res=[list1[i]]
        #         elif i + j == minn:
        #             res.append(list1[i]) 
    
        # return res 
