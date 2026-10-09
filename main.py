from sln import *

def main():
    matrix : list[list[int]] = [
        [-2, -3, 3],
        [-5, -10, 1],
        [10, 30, -5]
    ]

    result : int = brute_force(matrix)

    print("brute force sln is: " + str(result))

if __name__ == "__main__":
    main()
