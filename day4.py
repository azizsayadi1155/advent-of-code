# PART 1

import numpy as np

def count_word(grid, word, start_row, start_col, delta_row, delta_col):
    for k in range(len(word)):
        r, c = start_row + k * delta_row, start_col + k * delta_col
        if not (0 <= r < grid.shape[0] and 0 <= c < grid.shape[1]) or grid[r][c] != word[k]:
            return 0
    return 1

grid = np.array([list(line.strip()) for line in open("input.txt")])
directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
word = "XMAS"

print("Result =", sum(count_word(grid, word, i, j, dr, dc) for i in range(grid.shape[0]) for j in range(grid.shape[1]) for dr, dc in directions))


# PART 2

def count_x_mas(grid, r, c):
    rows, cols = grid.shape
    tl_br = [(r - 1, c - 1), (r + 1, c + 1)]
    tr_bl = [(r - 1, c + 1), (r + 1, c - 1)]
    if all(0 <= x < rows and 0 <= y < cols for x, y in tl_br + tr_bl):
        tl_br_chars = grid[tl_br[0]] + grid[r, c] + grid[tl_br[1]]
        tr_bl_chars = grid[tr_bl[0]] + grid[r, c] + grid[tr_bl[1]]
        return int(tl_br_chars in {"MAS", "SAM"} and tr_bl_chars in {"MAS", "SAM"})
    return 0

grid = np.array([list(line.strip()) for line in open("input.txt")])
print("Result =", sum(count_x_mas(grid, i, j) for i in range(1, grid.shape[0] - 1) for j in range(1, grid.shape[1] - 1) if grid[i, j] == "A"))

