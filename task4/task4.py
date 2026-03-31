## Task 4
import sys
import numpy as np


def calc(nums: list) -> str:
    mean = round(np.mean(nums), 0)
    steps = sum([int(abs(x - mean)) for x in nums])
    if steps < 20:
        return str(steps)
    else:
        return "20 ходов недостаточно для приведения всех элементов массива к одному числу"
    


if __name__ == "__main__":

    with open(sys.argv[1]) as f:
        nums = [int(i.strip()) for i in f.readlines()]

    print(calc(nums))