class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        vis = set()

        def dfs(room):
            vis.add(room)
            for key in rooms[room]:
                if key not in vis:
                    dfs(key)

        print(vis)
        dfs(0)
        return len(vis) == len(rooms)

        