#200917_programmers_level1_시저암호_python
def solution(s, n):
    answer = []
    
    my_list= list(s)
    for i in my_list:
        if not i.isalpha():
            answer.append(i)
        else:
            if 65 <= ord(i) <= 90 :
                if ord(i)+n>90:
                    answer.append(chr(ord(i)+n-26))
                else:
                    answer.append(chr(ord(i)+n))
            else:
                if ord(i)+n>122: 
                    answer.append(chr(ord(i)+n-26))
                else:
                    answer.append(chr(ord(i)+n))

                    
        
    return ''.join(answer)
