def solution(seoul):
    str=""
    for id, val in enumerate(seoul) :
        if val =="Kim":
            return "김서방은 %d에 있다"%id
