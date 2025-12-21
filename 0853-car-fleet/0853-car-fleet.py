class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos = [[p,s] for p,s in zip(position, speed)]
        pos.sort()

        stack = []

        for i in range(len(pos)-1, -1,-1):
            pr = pos[i]
            p = pr[0]
            s = pr[1]

            time = (target-p)/s
            stack.append(time)

            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)    
        