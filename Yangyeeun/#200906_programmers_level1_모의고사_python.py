#200906_programmers_level1_모의고사_python
def solution(answers):
    counts = [0,0,0]#점수를 측정하고
    winner = []#가장 많이 맞춘사람을 찾는다
    s1 = [1, 2, 3, 4, 5]
    s2 = [2, 1, 2, 3, 2, 4, 2, 5]
    s3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5,]
    
    for i in range(len(answers)): #answers와 답안지 앞에서부터 비교
        if answers[i] == s1[(i%5)]:
            counts[0] += 1
        if answers[i] == s2[(i%8)]:
            counts[1] += 1
        if answers[i] == s3[(i%10)]:
            counts[2] += 1
            
    for i in range(3): 
        if counts[i] == max(counts): #최고점수이면
            winner.append(i+1) # 반환

    return winner
