class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        dec = {}
        left = 0
        max_val = 0

        for i in range(len(fruits)):
            dec[fruits[i]] = dec.get(fruits[i], 0)+1

            while len(dec) > 2 and left < len(fruits):
                dec[fruits[left]] -= 1
                if dec[fruits[left]] == 0:
                    del dec[fruits[left]]
                left += 1
            max_val = max(max_val, sum(dec.values()))
            
        return max_val
