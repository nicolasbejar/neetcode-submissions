from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def getAdjacents(i, j):
            ans = []
            directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

            for dr, dc in directions:
                r, c = i + dr, j + dc
                if 0 <= r < len(board) and 0 <= c < len(board[0]):
                    ans.append((r, c))

            return ans

        visited = set()

        def dfs(i, j, idx):
            if board[i][j] != word[idx]:
                return False

            if idx == len(word) - 1:
                return True

            visited.add((i, j))

            for r, c in getAdjacents(i, j):
                if (r, c) not in visited:
                    if dfs(r, c, idx + 1):
                        visited.remove((i, j))
                        return True

            visited.remove((i, j))
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True

        return False