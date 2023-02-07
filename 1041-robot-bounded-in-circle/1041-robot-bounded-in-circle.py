class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
       
        idx = 0
        x = 0
        y = 0
        angle = 0
        while idx < len(instructions):
            while idx < len(instructions) and instructions[idx] == 'G':
                if angle == 0:
                    y += 1
                elif angle == -180 or angle == 180:
                    y -= 1
                elif angle == -90 or angle == 270:
                    x += 1
                elif angle == 90 or angle == -270:
                    x -= 1
                idx += 1
            while idx < len(instructions) and instructions[idx] == 'L':
                angle = (angle - 90) % 360
                idx += 1
            while idx < len(instructions) and instructions[idx] == 'R':
                angle = (angle + 90) % 360
                idx += 1
        if (x != 0 or y != 0) and angle == 0:
            return False
        return True

        