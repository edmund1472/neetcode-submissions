from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m = len(grid)
        n = len(grid[0])

        q = deque()

        # Put every treasure into the queue
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    q.append((i, j))

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while q:
            i, j = q.popleft()

            for di, dj in directions:
                ni = i + di
                nj = j + dj

                # invalid or not INF
                if (
                    ni < 0 or ni >= m or
                    nj < 0 or nj >= n or
                    grid[ni][nj] != 2147483647
                ):
                    continue

                grid[ni][nj] = grid[i][j] + 1
                q.append((ni, nj))