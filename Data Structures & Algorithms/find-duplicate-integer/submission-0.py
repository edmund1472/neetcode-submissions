class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[0]

        # Find the cycle
        while True:
            slow = nums[slow]          # move 1 step
            fast = nums[nums[fast]]    # move 2 steps

            if slow == fast:
                break

        # Find the start of the cycle
        slow = nums[0]

        while slow != fast:
            slow = nums[slow]          # both move 1 step
            fast = nums[fast]

        # Start of cycle = duplicate
        return slow