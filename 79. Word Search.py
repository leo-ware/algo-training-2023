def exists(board, word, visited, pos):
    x, y = pos
    for i, j in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
        x1 = x + i
        y1 = y + j
        
        if (
            0 <= x1 < len(board) and
            0 <= y1 < len(board[0]) and
            (x1, y1) not in visited
            ):
            if board[x1][y1] == word[0]:
                if len(word) == 1:
                    return True
                
                pos = (x1, y1)
                nv = visited.copy()
                nv.add(pos)
                if exists(board, word[1:], nv, pos):
                    return True


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for x in range(len(board)):
            for y in range(len(board[0])):
                if board[x][y] == word[0]:
                    if len(word) == 1:
                        return True
                    if exists(board, word[1:], {(x, y)}, (x, y)):
                        return True
        return False
