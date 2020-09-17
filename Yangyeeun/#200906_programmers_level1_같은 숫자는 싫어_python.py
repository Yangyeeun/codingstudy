#200906_programmers_level1_같은 숫자는 싫어_python
def solution(arr):
    answer=[]
    answer.append(arr[0]) #0번째 원소를 배열에 담고
    for i in range(1,len(arr)-1): #1번째 ~ 배열끝까지 수행
        if arr[i] != arr[i+1]: # 만약 이 원소가 다음 원소랑 다르면
            answer.append(arr[i+1]) #배열에 추가
    return answer
