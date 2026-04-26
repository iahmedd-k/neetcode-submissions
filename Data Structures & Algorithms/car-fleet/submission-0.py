from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = sorted(zip(position, speed), reverse=True)
        stack = []

        for pos, spd in pairs:
            time = (target - pos) / spd
            stack.append(time)

            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
 
        return len(stack)

        # if new time is greateer than the previous time keep the stack orthewise pop the stack