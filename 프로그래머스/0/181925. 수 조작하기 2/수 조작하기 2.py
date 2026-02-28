def solution(numLog):
    answer = []
    dic = { 1 : "w", -1 : "s", 10 : "d", -10 : "a"}
    for i in range (1, len(numLog)):
        log = numLog[i] - numLog[i-1]
        answer.append(dic[log])
    return "".join(answer)