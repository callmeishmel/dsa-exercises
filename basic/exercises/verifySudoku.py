class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = self.areRowsValid(board)

        cols = self.areRowsValid(list(zip(*board[::-1])))

        if rows is True and cols is True:
            return True
        
        return False

    def areRowsValid(self, board: List[List[str]]) -> bool:
        for i, array in enumerate(board):
            # Check rows
            rowPrevs = []
            for val in array:
                if val != '.':
                    if val in rowPrevs:
                        return False
                    rowPrevs.append(val)
        return True