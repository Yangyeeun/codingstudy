#programmers_level1_완주하지 못한 선수_python
def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i,j in zip(participant,completion):
        if i !=j:
            return i
    return participant[-1]

A = ['a','b','c'] #맨뒤-> 마지막값     
B = ['a','b']
print(list(zip(A, B)))

A = ['a','b','c']  #맨뒤아닌위치 -> zip의 차이난 part의 원소
B = ['b','c']
print(list(zip(A, B))) #[('a', 'b'), ('b', 'c')]

#동명이인처리
A = ['a','b','b'] #동명이인 맨뒤-> 마지막값      
B = ['a','b']
print(list(zip(A, B)))


A = ['a','a','b']  #동명이인 맨뒤아닌위치-> zip의 차이난 part의 원소     
B = ['a','b']
print(list(zip(A, B)))
