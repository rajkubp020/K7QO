class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = dict()
        for id,i in enumerate(nums):
            sec=target-i



            if sec not in store:
                 store[i]=id

            else:
                return [store[sec],id]
                
