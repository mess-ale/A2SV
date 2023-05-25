class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = 0
        ten = 0
        for bill in bills:
            if bill == 5:
                five += 1
            else:
                if bill == 10:
                    if five:
                        ten += 1
                        five -= 1
                    else:
                        return False
                
                elif bill == 20:
                    if five:
                        five -= 1
                        if ten:
                            ten -= 1
                        elif five >= 2:
                            five -= 2
                        else:
                            return False
                    else:
                        return False

        return True