class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        ress = []
        flag = True
        res = ''
        for s in source:
            i = 0
            while i  <  len(s):
                if flag:

                    if i == len(s) -1:
                        res += s[i]
                    else:
                        t = s[i:i+2]
                        if t == "/*":
                            flag = False
                            i +=2
                            continue
                        elif t == '//':
                            break
                        else:
                            res += s[i] 
                        
                else:
                    t = s[i: i+2]
                    if t == '*/':
                        flag = True
                        i += 2 
                        continue 
                i += 1

            if flag and res:
                ress.append(res)
                res = ''
        # s = ""
        
    
        return ress         
