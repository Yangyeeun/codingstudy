def solution(s):
    pCount =s.count('p')+s.count('P')
    yCount = s.count('y')+s.count('Y')
    if pCount==yCount:
         return True
    else:
        return False
