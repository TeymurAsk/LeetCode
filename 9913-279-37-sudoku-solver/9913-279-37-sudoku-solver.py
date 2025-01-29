class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        rows = [set() for _ in range(9)] # numbers used in row
        cols = [set() for _ in range(9)] # numbers used in col
        boxes = [[set() for _ in range(3)] for _ in range(3)] # numbers used in box
        empty_cells = [] # cells that are empty
        for i, row in enumerate(board): # collect numbers in row / col / box, add empty to empty_cells
            for j, value in enumerate(row):
                if value != ".": 
                    rows[i].add(value)
                    cols[j].add(value)
                    boxes[i//3][j//3].add(value)
                else:
                    empty_cells.append((i, j)) 

        # [ (number of available options for cell), i, j] 
        empty_cells = [
            (9-len(rows[i] | cols[j] | boxes[i//3][j//3]), i, j)
            for i, j in empty_cells
        ]
        heapq.heapify(empty_cells) # sort by lowest amount of available numbers

        def dfs() -> bool:
            if not empty_cells: # all cells are filled
                return True

            _, i, j = heapq.heappop(empty_cells)
            row = rows[i]
            col = cols[j]
            box = boxes[i//3][j//3]
            cell_options = 0  
            for value in '123456789': # check possible numbers for each cell
                if (value in row or value in col or value in box): 
                    continue # skip if number present in row, col, or box

                board[i][j] = value # add number to board and row / col / box
                row.add(value)
                col.add(value)
                box.add(value)

                if dfs(): # try to fill in rest of board
                    return True

                row.remove(value) # couldn't fill rest of board, take out used number
                col.remove(value)
                box.remove(value)
                cell_options += 1 # didn't use value, add another option for cell

            heapq.heappush(empty_cells, (cell_options, i, j)) # re-add current cell w/ num options
            return False
            
        dfs()