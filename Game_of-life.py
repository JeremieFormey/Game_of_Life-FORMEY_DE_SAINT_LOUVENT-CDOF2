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
    """Counts the live neighbors of a cell with toroidal wrapping."""
    neighbors = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),          (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]
    count = 0
    for dx, dy in neighbors:
        nx = (x + dx) % grid.shape[0]  # Wrap around top/bottom
        ny = (y + dy) % grid.shape[1]  # Wrap around left/right
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

def get_initial_configuration(rows, cols):
    """Allows the user to set the initial configuration of the grid."""
    grid = np.zeros((rows, cols), dtype=int)
    print("\033[93mCreate your initial configuration!\033[0m")
    print(f"Enter cell coordinates as 'x,y' (e.g., '2,3'). Type 'done' to finish.")
    print_grid(grid)

    while True:
        user_input = input("Enter coordinates (or 'done'): ").strip()
        if user_input.lower() == "done":
            break
        try:
            x, y = map(int, user_input.split(","))
            if 0 <= x < rows and 0 <= y < cols:
                grid[x, y] = 1
                clear_console()
                print_grid(grid)
            else:
                print("\033[91mCoordinates out of bounds. Try again.\033[0m")
        except ValueError:
            print("\033[91mInvalid input. Please enter coordinates as 'x,y'.\033[0m")
    return grid

def main():
    # Define the grid size
    rows, cols = 20, 20

    # Get the initial configuration from the user
    clear_console()
    grid = get_initial_configuration(rows, cols)

    generation = 0
    while True:
        clear_console()
        print(f"Game of Life (Toroidal Space) - Generation {generation}")
        print_grid(grid)
        grid = update_grid(grid)
        generation += 1
        time.sleep(0.5)  # Pause between generations

if __name__ == "__main__":
    main()
