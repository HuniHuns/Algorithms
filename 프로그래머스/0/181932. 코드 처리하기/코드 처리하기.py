def solution(code):
    answer = "".join(code.split("1"))[::2] or "EMPTY"
    return answer