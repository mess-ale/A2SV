class Solution:
    
    def __init__(self ):
        self.ans = []


    def permute(self, nums: List[int]) -> List[List[int]]:
        
        n = ( 1 << len(nums) )- 1
        self.solve( nums , n , 0 , [] ) 
        return self.ans 
        
    def solve( self , nums , n , cur_mask , temp ):
        
        if n == cur_mask :
            self.ans.append( temp )
            return 
        
        sz = len( nums )
        for i in range( sz ):
            if cur_mask & ( 1 << i ) == 0 :
                temp.append( nums[i] )
                self.solve( nums , n , cur_mask | ( 1 << i )  , temp.copy() )
                temp.pop()