class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        groups = {}

        for i in nums:
            if i not in groups:
                groups[i] = 0
            groups[i] += 1
        
        sorteded = sorted(groups, key = groups.get, reverse = True)
        return sorteded[:k]