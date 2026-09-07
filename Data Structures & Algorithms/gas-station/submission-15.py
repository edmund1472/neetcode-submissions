class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        sum_gas = 0
        sum_cost = 0
        for i in range(len(gas)):
            sum_gas += gas[i]

        for j in range(len(cost)):
            sum_cost += cost[j]

        if sum(gas) < sum(cost):
            return -1
        total = 0
        answer = 0

        for i in range(len(gas)):
            total += gas[i] - cost[i]

            if total < 0:
                total = 0
                answer = i + 1

        return answer
        total = 0 
        answer = -1
        for k in range(len(gas)):
            total += gas[k]
            total -= cost[k]
            if total < 0:
                continue
            answer = i
        return answer

        
