class Solution:
    def average(self, salary: List[int]) -> float:
        
        min_value = 1000001
        max_value = 0
        for i in range(len(salary)):
            min_value = min(min_value, salary[i])
            max_value = max(max_value, salary[i])
        
        sums = 0
        count = 0
        for i in range(len(salary)):
            if salary[i]==max_value or salary[i]==min_value:
                continue
            else:
                sums += salary[i]
                count += 1
        return sums/count
