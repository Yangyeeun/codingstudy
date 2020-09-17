#0909_programmers_level1_문자열을 정수로 바꾸기_python
def strToInt(str): ##해결방안 생각!!:문자열을 거꾸로 표현한다면 -부호일때만 정수로 바꾼후에 부호를 바꾸면된다! 
    result = 0

    for idx, number in enumerate(str[::-1]):
        if number == '-':
            result *= -1
        else:
            result += int(number) * (10 ** idx)

    return result
