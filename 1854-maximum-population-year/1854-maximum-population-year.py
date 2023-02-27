class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        year_pop_count = dict()
        for i in range(1950, 2051):
            year_pop_count[i] = 0
        for log in logs:
            year_pop_count[log[0]] = year_pop_count.get(log[0]) + 1
            year_pop_count[log[1]] = year_pop_count.get(log[1]) - 1
        
        maxNum = year_pop_count[1950]
        maxYear = 1950

        for i in range(1950+1, 2051):
            year_pop_count[i] += year_pop_count[i-1]
            if year_pop_count[i] > maxNum:
                maxNum = year_pop_count[i]
                maxYear = i
            
        return maxYear
        