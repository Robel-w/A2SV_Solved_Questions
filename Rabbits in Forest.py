class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        cnt = Counter(answers)
        tot_rabbits = 0
        for k, v in cnt.items():
            group_size = k + 1
            num_groups = (v+k)//group_size
            tot_rabbits += group_size * num_groups
        return tot_rabbits   
