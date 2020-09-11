#200911_programmers_level1_소수 찾기_python
def solution(n):
    num= set(range(2, n+1)) #모든 수를 소수의 집합으로 넣고    
    for i in range(2, n+1):
    	if i in num: #집합의 최소에서
        	num -= set(range(2*i, n+1, i) # 그 수의 배수를 제거한다
    return len(sum)
    
