class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                ele = board[i][j]
                
                if ele == ".":
                    continue

                box_idx = (i//3) *3 + (j//3)
                if ele in rows[i] or ele in cols[j] or ele in boxes[box_idx]:
                    return False

                rows[i].add(ele)
                cols[j].add(ele)
                boxes[box_idx].add(ele)
        return True