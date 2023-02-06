class DetectSquares:
    def __init__(self):
        self.dict1 = defaultdict(int)

    def add(self, point):
        self.dict1[tuple(point)] += 1

    def count(self, point):
        total = 0
        x1, y1 = point
    
        for x, y in self.dict1:
            if (x, y1) in self.dict1 and (x1, y) in self.dict1 and abs(x - x1) == abs(y - y1) and x != x1:
                total += self.dict1[(x,y)]*self.dict1[(x,y1)]*self.dict1[(x1,y)]
            
        return total


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)