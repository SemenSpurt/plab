## Task 1
import sys


def calculate_path(n: int , m: int ) -> str:
    seq = list(range(1, n + 1))
    nxt_el = m - 1
    path = [1]
    
    while seq[nxt_el % n] != 1:
        path.append(seq[nxt_el % n])
        nxt_el += m - 1
    else:
        return "".join([str(i) for i in path])


if __name__ == "__main__":

    args = [int(i) for i in sys.argv[1:]]

    if len(args) % 2 != 0:
        raise ValueError('There should be equal amount of n and m')
    
    for [n, m] in zip(args[:-1:2], args[1::2]):

        if (n < 1) or (m < 1):
            raise ValueError('Arguments n and m should be positive integers')
        else:
            print(calculate_path(n, m), end="")