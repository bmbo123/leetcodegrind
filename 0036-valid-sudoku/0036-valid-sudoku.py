class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = defaultdict(set)
        cols = defaultdict(set)
        square = defaultdict(set)
        
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == ".":
                    continue
                if board[r][c] in rows[r]:
                    return False
                if board[r][c] in cols[c]:
                    return False
                    
                
                sr = r //3
                sc = c //3
                
                if board[r][c] in square[(sr,sc)]:
                    return False
                
                square[(sr,sc)].add(board[r][c])
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                
        return True
