class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        skills = skill[0] + skill[-1]
        l, r = 1, len(skill)-2
        summ = skill[0] * skill[-1]
        while l < r:
            if skills != skill[l]+skill[r]:
                return -1
            summ += skill[l] * skill[r]    
            l += 1
            r -=1
        return summ      
        
