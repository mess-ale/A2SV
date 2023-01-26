class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        i = 0
        j = len(people) - 1
        count = 0
        while i <= j:
            temp = people[i] + people[j]
            if i == j:
                temp = temp // 2
            if temp <= limit:
                count += 1
                i += 1
                j -= 1
            else:
                count += 1
                j -= 1
        return count