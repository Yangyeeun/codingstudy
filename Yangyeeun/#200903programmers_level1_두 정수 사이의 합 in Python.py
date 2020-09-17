#programmers/level1]두 정수 사이의 합 in Python
def solution(a, b):
    if a==b:
        return a
    elif a>b:
        return(sum(list(range(b,a+1))))
    else:
        return(sum(list(range(a,b+1))))
    
    
print(solution(3,5))
