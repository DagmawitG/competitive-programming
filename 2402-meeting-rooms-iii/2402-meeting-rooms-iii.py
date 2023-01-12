class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetingRoom = []
        totalRooms = [i for i in range(n)]
        count = [0] * n
        meetings.sort()
        
        for start, end in meetings:
            while meetingRoom and meetingRoom[0][0] <= start:
                endRoom, room = heapq.heappop(meetingRoom)
                heapq.heappush(totalRooms, room)
                
            if totalRooms:
                room = heapq.heappop(totalRooms)
                heapq.heappush(meetingRoom, (end,room))
            else:
                time, room = heapq.heappop(meetingRoom)
                heapq.heappush(meetingRoom,(time+ end-start, room))
            count[room] += 1
        return count.index(max(count))
        