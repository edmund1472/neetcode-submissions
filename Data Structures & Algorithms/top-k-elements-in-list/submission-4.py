class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        # Count frequencies
        for num in nums:
            if num not in count:
                count[num] = 0
            count[num] += 1

        # Create frequency buckets
        buckets = [[] for i in range(len(nums) + 1)]

        # Put each number into its frequency bucket
        for num, freq in count.items():
            buckets[freq].append(num)

        result = []

        # Highest frequency -> lowest frequency
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                result.append(num)

                if len(result) == k:
                    return result