class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = []
        ten = []
        for bill in bills:
            if bill == 5:
                five.append(bill)
            else:
                if bill == 10:
                    if five:
                        ten.append(bill)
                        five.pop()
                    else:
                        return False
                
                elif bill == 20:
                    if five:
                        five.pop()
                        if ten:
                            ten.pop()
                        elif len(five) >= 2:
                            five.pop()
                            five.pop()
                        else:
                            return False
                    else:
                        return False

        return True