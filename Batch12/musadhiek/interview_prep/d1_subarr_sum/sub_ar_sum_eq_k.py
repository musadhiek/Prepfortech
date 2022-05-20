class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #use a hash map store the prefix sum count
        #increament result with count when prefix sum - target in hash map
        
        prefix = {0:1}
        cur_sum = 0
        res = 0
        
        for num in nums:
            cur_sum += num
            diff = cur_sum - k 
            res += prefix.get(diff,0)
            prefix[cur_sum] = 1+ prefix.get(cur_sum,0)
        return res