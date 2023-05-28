class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memory = [0]*(len(cost)+1)
        cost.append(0)
        def depy(n):
            if n == 0 or n == 1:
                return cost[n]
            
            if not memory[n]:
                memory[n] = min(depy(n-1), depy(n-2)) + cost[n]
                
            return memory[n]
                
        return depy(len(cost)-1)