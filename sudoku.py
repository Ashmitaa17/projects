def solveSudoku(self, board: List[List[str]]) -> None:
        def check(board, i, j, nums):
            if nums in board[i]:
                return False
            elif nums in [board[row][j] for row in range(9)]:
                return False
            startrow, startcol= (i//3)*3, (j//3)*3
            for r in range(startrow, startrow+3):
                for c in range(startcol, startcol+3):
                    if board[r][c]==nums:
                        return False
            return True
        
        def rec(board, i ,j):
            if j==9:
                i+=1
                j=0
            if i==9:
                return True
            if board[i][j]==".":
                for num in range(1, 10):
                    numstr=str(num)
                    if (check(board, i, j, numstr)):
                        board[i][j]=numstr
                        if (rec(board, i, j+1)):
                            return True
                        board[i][j]="."
                return False
            
            else:
                return rec(board, i, j+1)

        rec(board,0,0)
        return board
        
