import sys
import math

def brute_force(matrix : list[list[int]]) -> int:
    all_sums : list[int] = []
    brute_force_rec(matrix, all_sums, 0, 0, 0, True, "")

    is_negative : bool = False
    abs_min = all_sums[0]

    for sum in all_sums:
        print(sum)
        is_negative = sum < 0
        abs_min = min(abs_min, abs(sum))

    return (abs_min + 1 if is_negative else abs_min)

def brute_force_rec (
    matrix : list[list[int]],
    all_sums: list[int],
    curr_sum: int,
    curr_x : int,
    curr_y : int,
    to_down : bool,
    indent : str
) -> None:
    if curr_x >= len(matrix) or curr_y >= len(matrix[0]) or curr_x < 0 or curr_y < 0:
        print(indent + ("└── " if to_down else "├── ") + "nil")
        return

    curr_sum += matrix[curr_x][curr_y]

    # print all ways
    print(indent + ("└── " if to_down else "├── ") + str(matrix[curr_x][curr_y]) + " sum (" + str(curr_sum) + ")")

    if curr_x == len(matrix) - 1 and curr_y == len(matrix[0]) - 1:
        all_sums.append(curr_sum)
        return

    # go to left
    brute_force_rec(
        matrix,
        all_sums,
        curr_sum,
        curr_x + 1,
        curr_y,
        False,
        indent + ("    " if to_down else "│   ")
    )

    # go to down
    brute_force_rec(
        matrix,
        all_sums,
        curr_sum,
        curr_x,
        curr_y + 1,
        True,
        indent + ("    " if to_down else "│   ")
    )

def bottom_up(matrix : list[list[int]]) -> int:
    rows : int = len(matrix)
    cols : int = len(matrix[0])
    dp : list[list[int]] = [[0] * cols for i in range(rows)]

    # base cases
    dp[0][0] = matrix[0][0]

    for col in range(1, cols):
        dp[0][col] = matrix[0][col] + dp[0][col - 1]

    for row in range(1, rows):
        dp[row][0] = matrix[row][0] + dp[row - 1][0]

    for row in range(1, rows):
        for col in range(1, cols):
            dp[row][col] = -min(abs(dp[row - 1][col]), abs(dp[row][col - 1])) + matrix[row][col]

    # debugging
    for i in range(rows):
        for j in range(cols):
            print(str(dp[i][j]), end=" ")
        print()

    last : int = dp[rows - 1][cols - 1]
    return (abs(last) + 1 if last < 0 else last)

def bottom_up_opt(matrix : list[list[int]]) -> int:
    rows : int = len(matrix)
    cols : int = len(matrix[0])

    dp : list[int] = [0] * rows
    dp[0] = matrix[0][0]

    for col in range(1, cols):
        dp[col] = matrix[0][col] + dp[col - 1]

    for row in range(1, rows):
        dp[0] += matrix[row][0]
        for col in range(cols):
            dp[col] = min(abs(dp[col - 1]), dp[col]) + matrix[row][col]

    last : int = dp[rows - 1]
    return (abs(last) + 1 if last < 0 else last)

def top_down(matrix : list[list[int]]) -> int:
    rows : int = len(matrix)
    cols : int = len(matrix[0])

    arr : list[list[int]] = [[sys.maxsize] * cols for i in range(rows)]

    # base cases
    arr[0][0] = matrix[0][0]

    for col in range(1, cols):
        arr[0][col] = matrix[0][col] + arr[0][col - 1]

    for row in range(1, rows):
        arr[row][0] = matrix[row][0] + arr[row - 1][0]

    result = top_down_ref(matrix, arr, rows - 1, cols - 1, True, "")

    # debugging
    for i in range(rows):
        for j in range(cols):
            print(str(arr[i][j]), end=" ")
        print()

    return result if result > 0 else -result + 1

def top_down_ref(matrix : list[list[int]], arr : list[list[int]], curr_x : int, curr_y : int, to_down : bool, indent : str) -> int:
    if (curr_x >= len(matrix) or curr_y >= len(matrix[0]) or curr_x < 0 or curr_y < 0):
        return sys.maxsize

    print(indent + ("└── " if to_down else "├── ") + str(matrix[curr_x][curr_y]))

    if (arr[curr_x][curr_y] != sys.maxsize):
        return arr[curr_x][curr_y]

    right = top_down_ref(
        matrix,
        arr,
        curr_x - 1,
        curr_y,
        False,
        indent + ("    " if to_down else "│   ")
    )

    down = top_down_ref(
        matrix,
        arr,
        curr_x,
        curr_y - 1,
        True,
        indent + ("    " if to_down else "│   ")
    )

    if abs(right) < abs(down):
        arr[curr_x][curr_y] = right + matrix[curr_x][curr_y]
    else:
        arr[curr_x][curr_y] = down + matrix[curr_x][curr_y]

    return arr[curr_x][curr_y]
