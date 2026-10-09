from sln import *

def main():
    matrix : list[list[int]] = [
        [-2, -3, 3],
        [-5, -10, 1],
        [10, 30, -5]
    ]

    result : int = brute_force(matrix)
    print("brute force sln is: " + str(result))

    btm_up : int = bottom_up(matrix)
    print("bottom up sln is: " + str(btm_up))

    btm_up_opt : int = bottom_up_opt(matrix)
    print("bottom up sln is: " + str(btm_up_opt))

    tp_down : int = top_down(matrix)
    print("bottom up sln is: " + str(tp_down))

if __name__ == "__main__":
    main()
