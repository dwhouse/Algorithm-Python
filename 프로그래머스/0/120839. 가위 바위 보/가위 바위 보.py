def solution(rsp):
    answer = ""
    for s in rsp:
        if s == "0":
            answer += "5"
        elif s == "2":
            answer += "0"
        else:
            answer += "2"
    return answer