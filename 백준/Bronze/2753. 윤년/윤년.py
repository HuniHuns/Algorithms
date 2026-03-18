""" solve.py for 2753. 윤년 """

import sys

def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(year: int) -> int:
    return int(year%400 == 0 or year%4 == 0 and year%100 != 0)



def main() -> None:
    year = int(sys_input())
    answer:int = solve(year)
    print(answer)


if __name__ == "__main__":
    main()