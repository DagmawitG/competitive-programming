class Solution:
    def racecar(self, target: int) -> int:
        q = deque([(0, 0, 1)])
        
        while q:
            step, position, speed = q.popleft()
            if position == target:
                return step
            q.append((step + 1, position + speed, speed * 2))
            if position + speed > target and speed > 0:
                q.append((step + 1, position, -1))
            if position + speed < target and speed < 0:
                q.append((step + 1, position, 1))
