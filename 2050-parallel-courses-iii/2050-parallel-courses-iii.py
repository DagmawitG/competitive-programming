class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        indegree = [0] * (n + 1)
        graph = defaultdict(list) #key - int, value - list[nodes]
        
        for incoming,outgoing in relations:
            indegree[outgoing] += 1
            graph[incoming].append(outgoing)
        
        queue = deque()
        end_time = defaultdict(int)
        max_time = defaultdict(int)
        
        for i in range(1,n + 1):
            if indegree[i] == 0:
                queue.append(i)
        
        while(queue):
            node = queue.popleft()
            end_time[node] = time[node - 1] + max_time[node]
            
            for course in graph[node]:
                indegree[course] -= 1
                max_time[course] = max(max_time[course],end_time[node])
                if indegree[course] == 0:
                    queue.append(course)
        
        return max(end_time.values())

        
        
        
        