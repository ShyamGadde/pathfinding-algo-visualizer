import os
import random
import time

START = "\033[92m S \033[0m"
END = "\033[92m E \033[0m"
WALL = "\033[91m ▓ \033[0m"
OPEN_SPACE = "\033[94m ◌ \033[0m"
PATH = "\033[92m ◍ \033[0m"
ROW_SEPARATOR = "---+"
COLUMN_SEPARATOR = "|"
COMMAND = "cls" if os.name == "nt" else "clear"


def generate_maze(size, wall_percentage):
    elements = [WALL, OPEN_SPACE]
    weights = [wall_percentage / 100, 1 - wall_percentage / 100]
    maze = [random.choices(elements, weights, k=size) for _ in range(size)]
    maze[0][0], maze[size - 1][size - 1] = OPEN_SPACE, OPEN_SPACE
    return maze


def print_maze(maze):
    os.system(COMMAND)
    maze[0][0], maze[len(maze) - 1][len(maze) - 1] = START, END

    print("\n+" + ROW_SEPARATOR * len(maze[0]))
    for row in maze:
        print(f"{COLUMN_SEPARATOR}{COLUMN_SEPARATOR.join(row)}{COLUMN_SEPARATOR}")
        print("+" + ROW_SEPARATOR * len(row))

    maze[0][0], maze[len(maze) - 1][len(maze) - 1] = OPEN_SPACE, OPEN_SPACE


def find_path_dfs(maze, current, end):
    time.sleep(0.1)
    row, col = current
    if not (
        0 <= row < len(maze)
        and 0 <= col < len(maze[0])
        and maze[row][col] == OPEN_SPACE
    ):
        return False
    if current == end:
        maze[row][col] = PATH
        print_maze(maze)
        return True

    maze[row][col] = PATH
    print_maze(maze)

    neighbors = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
    for neighbor in neighbors:
        if find_path_dfs(maze, neighbor, end):
            return True

    maze[row][col] = OPEN_SPACE
    print_maze(maze)
    return False


def solver():
    # size = int(input("Enter the size of the maze: "))
    size = 10
    wall_percentage = 25
    maze = None

    option = 2

    while True:
        if option == 1:
            if find_path_dfs(maze, (0, 0), (size - 1, size - 1)):
                print("\nPath Found!")
            else:
                print("\nNo Path Found!")
        elif option == 2:
            print("Generated Maze: ")
            maze = generate_maze(size, wall_percentage)
            print_maze(maze)
        elif option == 3:
            print("Exiting...")
            break
        else:
            print("Invalid option!")

        print("\nOptions:")
        print("1. Find Path")
        print("2. Generate Another Maze")
        print("3. Exit")
        option = int(input("# [1/2/3]: "))


if __name__ == "__main__":
    solver()
