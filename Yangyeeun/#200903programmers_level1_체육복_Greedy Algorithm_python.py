#[programmers/level1] 체육복_Greedy Algorithm_python
def solution(n, lost, reserve):
    #진짜 옷의 개수를 세보자
    clothes_list=[1]*n #모든 학생은 옷을 기본하나 가지고 있고
    
    for i in reserve:
        clothes_list[i-1]=2 #여분을 가진 학생은 2개 가진다
        
    for i in lost:
        clothes_list[i-1]=clothes_list[i-1]-1 #분실한 학생은 빼준다
    
    for index,value in enumerate(clothes_list):
        #옷이 0개이고 앞 학생이 2벌 가지면 빌린다
            if value==0 and index> 0 and clothes_list[index-1]==2:
                clothes_list[index]=1
                clothes_list[index-1]=1
        #옷이 0개이고 뒤 학생이 2벌 가지면 빌린다
            if value==0 and index<n-1 and clothes_list[index+1]==2:
                clothes_list[index]=1
                clothes_list[index+1]=1
    return n - clothes_list.count(0)

solution(5,[2,4],[1,3,5])
