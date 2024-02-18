# Clarifications
# We don't need to solve the puzzle
# We only need to verify that the current state of the puzzle is valid
# What makes an invalid board
#   - Repeat numbers
#   - Are non numbers something we need to account for?
#   - Are all arrays guaranteed to have the same number (9x9)

# Naive method
# Iterate through each row and check if each num is unique in that space
# Iterate through each column and check if each num is unique in that space
# We don't need to check non number characters
#   - We can reduce the column/row array to just nums and check if unique (Unnecessary(?))
#   - We can IF number THEN check ignoring other characters (Direct)
# To check rows iterate through each array as they are
# To check columns iterate through each array at a specific index

# TODO This fails because I forgot to account for the rule where values
#      can't repeat inside a 3x3 grid 

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