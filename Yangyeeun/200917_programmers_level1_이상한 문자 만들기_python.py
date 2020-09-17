def solution(s):
    words_list = s.split(" ") #리스트를 공백단위로 쪼개자
    new_list = []
    for word in words_list: #리스트안 단어 하나씩 바꾸자
        new_words = "" #빈 문자열에 새문자로 바꿔 하나씩 넣어주자
        for i in range(len(word)):
            new_words += word[i].upper() if i%2 == 0 else word[i].lower() 
        new_list.append(new_words)#바꿔진 단어를 리스트에 넣자
    return " ".join(new_list)#리스트를 단어기준으로 문자열로 넣기
