#[programmers/level1]K번째수_python
def solution(array, commands):
    answer = []
    for command in commands:
        i,j,k= command[0],command[1],command[2]
        slice=sorted(array[i-1:j])
        answer.append(slice[k-1])
    return answer
