class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        
        path, travel, travel_taken, used = defaultdict(set), [source], 0, set()
        for i, route in enumerate(routes):
            for bus in route:
                path[bus].add(i)
        while travel:
            new = []
            for bus in travel:
                if bus == target:
                    return travel_taken
                for route in path[bus]:
                    if route not in used:
                        used.add(route)
                        for next_bus in routes[route]:
                            if next_bus != bus:
                                new.append(next_bus)
            travel_taken += 1
            travel = new
        return -1