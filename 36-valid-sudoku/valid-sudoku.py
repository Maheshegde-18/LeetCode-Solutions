class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rows=[set()for _ in range(9)]
        cols=[set()for _ in range(9)]
        boxes=[set()for _ in range(9)]
        for i in range(9):
            for j in range(9):
                nums=board[i][j]
                box=(i//3)*3+(j//3)
                if board[i][j]=='.':
                    continue
                if nums in rows[i]:
                    return False
                rows[i].add(nums)
                if nums in cols[j]:
                    return False
                cols[j].add(nums)
                if nums in boxes[box]:
                    return False
                boxes[box].add(nums)
        return True
        