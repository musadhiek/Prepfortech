class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        #all integers are postivie: use sliding window
        #increase size of window if less than target, check size decrease the size of window if greater than 
        #target
        
        lp , total = 0,0
        ans = float(inf)
        
        for rp in range(len(nums)):
            
            total += nums[rp]
            
            while total >= target:
                total -= nums[lp]
                ans = min(rp-lp+1,ans)
                lp += 1
        return 0 if ans == float(inf) else ans