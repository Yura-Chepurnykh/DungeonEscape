import sys
import math

def brute_force(matrix : list[list[int]]):
    all_sums : list[int] = []
    brute_force_rec(matrix, all_sums, 0, 0, 0, True, "")

    is_negative : bool = False
    abs_min = all_sums[0]

    for sum in all_sums:
        print(sum)
        is_negative = sum < 0
        abs_min = min(abs_min, abs(sum))

    return (abs_min + 1 if is_negative else abs_min)

def brute_force_rec(
    matrix : list[list[int]],
    all_sums: list[int],
    curr_sum: int,
    curr_x : int,
    curr_y : int,
    is_down : bool,
    indent : str
):
    if curr_x >= len(matrix) or curr_y >= len(matrix[0]) or curr_x < 0 or curr_y < 0:
        print(indent + ("└── " if is_down else "├── ") + "nil")
        return

    curr_sum += matrix[curr_x][curr_y]

    # print all ways
    print(indent + ("└── " if is_down else "├── ") + str(matrix[curr_x][curr_y]) + " sum (" + str(curr_sum) + ")")

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
        indent + ("    " if is_down else "│   ")
    )

    # go to down
    brute_force_rec(
        matrix,
        all_sums,
        curr_sum,
        curr_x,
        curr_y + 1,
        True,
        indent + ("    " if is_down else "│   ")
    )
