class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        stack = []
        pos_speed = []

        for i, v in enumerate(position):
            pos_speed.append((position[i], speed[i]))

        pos_speed.sort()

        for i in reversed(pos_speed):
            p, s = i
            time = (target - p)/s

            if stack and stack[-1]>=time:
                continue
                
            
            stack.append(time)



        return len(stack)