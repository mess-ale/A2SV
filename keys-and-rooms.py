class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        stor = set()
        stor.add(0)
        qe = deque()
        qe.append(rooms[0])
        visited = [rooms[0]]

        while qe:
            no = qe.popleft()
            visited.append(no)
            for i in no:
                stor.add(i)

            for i in no:
                if rooms[i] not in visited:
                    qe.append(rooms[i])

        if len(stor) == len(rooms):
            return True
        return False