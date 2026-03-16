""" solve.py for 10871. X보다_작은_수 """

import sys


def sys_input() -> str:
    return sys.stdin.readline().rstrip()


def solve(x: int, a: list[int]) -> list[int]:
    return [num for num in a if num < x]


def main() -> None:
    _, x = map(int, sys_input().split())
    a = list(map(int, sys_input().split()))
    answer: list[int] = solve(x, a)
    print(*answer)


if __name__ == "__main__":
    main()