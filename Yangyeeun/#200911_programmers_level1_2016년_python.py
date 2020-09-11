#programmers_level1_2016년_python
def solution(a, b):
    answer = ''
    days=0
    date=  [ "FRI", "SAT","SUN", "MON", "TUE", "WED", "THU", ]
    month=[ 31,29,31,30,31,30,31,31,30,31,30,31 ]
    for i in range(a-1):
        days += month[i]
    days+= b-1
    answer= date[days%7]
    return answer
