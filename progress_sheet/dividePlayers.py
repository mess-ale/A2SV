class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        test = skill[0] + skill[-1]
        i = 1
        j = len(skill) - 2
        while i < j:
            temp = skill[i] + skill[j]
            if test != temp:
                return -1
            i += 1
            j -= 1
        i = 0
        j = len(skill) - 1
        total = 0
        while i < j:
            total += skill[i] * skill[j]
            i += 1
            j -= 1
        return total