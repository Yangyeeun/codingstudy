#200924programmers_level1_문자열 내 마음대로 정렬하기_python
def solution(strings, n):
    return sorted(sorted(strings), key=lambda x:x[n])
