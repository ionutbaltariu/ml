from collections import deque


def maze_to_matrix(maze_file_name: str = "maze.in"):
    maze = []

    with open(maze_file_name, "r") as f:

        while line := f.readline():
            matrix_line = []

            for char in line.strip('\n'):
                matrix_line.append(char)

            maze.append(matrix_line)

    return maze


def get_possible_directions(i, j, matrix, matrix_row_num, matrix_col_num):
    # DOWN, RIGHT, UP, LEFT
    all_directions = {(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)}

    # can't go up
    if i == 0:
        all_directions.remove((i - 1, j))

    # can't do down
    if i == matrix_row_num - 1:
        all_directions.remove((i + 1, j))

    # can't go left
    if j == 0:
        all_directions.remove((i, j - 1))

    # can't go right
    if j == matrix_col_num - 1:
        all_directions.remove((i, j + 1))

    all_good_directions = set()

    for i, j in all_directions:
        if matrix[i][j] != "#":
            all_good_directions.add((i, j))

    return all_good_directions


def get_start_and_end(matrix):
    start_pos = -1, -1
    end_pos = -1, -1

    for i, line in enumerate(matrix):
        for j, el in enumerate(line):
            if el == "A":
                if start_pos == (-1, -1):
                    start_pos = i, j
                else:
                    raise Exception("Multiple start points found! Invalid maze!")
            if el == "B":
                if end_pos == (-1, -1):
                    end_pos = i, j
                else:
                    raise Exception("Multiple end points found! Invalid maze!")

    if start_pos == (-1, -1):
        raise Exception("Invalid maze! No start point given!")

    if end_pos == (-1, -1):
        raise Exception("Invalid maze! No end point given!")

    return start_pos, end_pos


def solve_maze(matrix):
    matrix_row_num = len(matrix)
    matrix_col_num = len(matrix[0])
    a, b = get_start_and_end(matrix)
    queue = deque()
    visited = set()
    queue.append((a, [a]))

    while queue:
        current_pos, journey = queue.pop()

        if current_pos in visited:
            continue

        visited.add(current_pos)

        if current_pos == b:
            print("Solution found!")
            return journey[:-1]

        i, j = current_pos
        all_moves = get_possible_directions(i, j, matrix, matrix_row_num, matrix_col_num)

        for move in all_moves:
            if move not in visited:
                queue.append((move, journey + [move]))

    print("No solution found!")
    return []


if __name__ == "__main__":
    matrix = maze_to_matrix()
    solved = solve_maze(matrix)

    if solved:
        print("The shortest path is the one with dots!")
        for i, j in solved:
            matrix[i][j] = "."

        for line in matrix:
            print(line)
