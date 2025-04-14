class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        tank = 0
        start = 0
        if sum(cost) > sum(gas):
            return -1
        for i in range(len(gas)):
            tank = gas[i] + tank
            if cost[i] > tank:
                start = i + 1
                tank = 0
            else:
                tank = tank - cost[i]
            print(tank)
        return start

