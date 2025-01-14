import numpy as np
import time
import os

def clear_console():
    """Clears the console for better display."""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_grid(grid):
    """Prints the grid to the console with enhanced visuals."""
    # Top border
    print("   " + "━" * (grid.shape[1] * 2 + 1))
    for i, row in enumerate(grid):
        line = " │ "  # Left border
        for cell in row:
            if cell:
                line += "\033[92m⬛\033[0m "  # Green for live cells
            else:
                line += "\033[90m⬜\033[0m "  # Grey for dead cells
        line += "│"  # Right border
        print(f"{i:2} {line}")  # Row index
    # Bottom border
    print("   " + "━" * (grid.shape[1] * 2 + 1))
    # Column indices
    print("    " + " ".join(f"{i:2}" for i in range(grid.shape[1])))

def get_neighbors(grid, x, y):
    """Counts the live neighbors of a cell."""
    neighbors = [
        (x - 1, y - 1), (x - 1, y), (x - 1, y + 1),
        (x, y - 1),             (x, y + 1),
        (x + 1, y - 1), (x + 1, y), (x + 1, y + 1)
    ]
    count = 0
    for nx, ny in neighbors:
        if 0 <= nx < grid.shape[0] and 0 <= ny < grid.shape[1]:
            count += grid[nx, ny]
    return count

def update_grid(grid):
    """Updates the grid for the next generation."""
    new_grid = np.zeros_like(grid)
    for x in range(grid.shape[0]):
        for y in range(grid.shape[1]):
            live_neighbors = get_neighbors(grid, x, y)
            if grid[x, y] == 1:  # Alive cell
                if live_neighbors in [2, 3]:
                    new_grid[x, y] = 1
            else:  # Dead cell
                if live_neighbors == 3:
                    new_grid[x, y] = 1
    return new_grid

def main():
    # Define the grid size and initial state
    rows, cols = 20, 20
    grid = np.zeros((rows, cols), dtype=int)

    # Create a simple pattern (e.g., a glider)
    grid[1, 2] = grid[2, 3] = grid[3, 1] = grid[3, 2] = grid[3, 3] = 1

    generation = 0
    while True:
        clear_console()
        print(f"Game of Life - Generation {generation}")
        print_grid(grid)
        grid = update_grid(grid)
        generation += 1
        time.sleep(0.5)  # Pause between generations

if __name__ == "__main__":
    main()
