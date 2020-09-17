def solution(n):
    answer = ''
   
    for i in range(n):
    	if i%2 ==1: #홀수이면 수추가
            answer+'수'
        elif i%2 ==0:#짝수이면 박추가
        	answer+'박'
    return answer
