class RandomizedSet:

    def __init__(self):
        self.vals = {}  
        self.indexs = []

    def insert(self, val: int) -> bool:
        if val in self.vals : return False 
        self.vals[val] = len(self.indexs)
        self.indexs.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val in self.vals: 
            lst = self.indexs[-1]     
            pos = self.vals[val]
            self.vals[lst] = pos         
            self.indexs[pos] = lst       
            self.vals.pop(val)           
            self.indexs.pop()            
            
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.indexs)

