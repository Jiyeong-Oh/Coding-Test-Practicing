import itertools
def solution(word):
    word_lst = ["A","E","I","O","U"]
    count=0
    for i in range(len(word)):
        count+=word_lst.index(word[i])*(sum(list(map(lambda x: 5**x, range(5-i)))))
        count+=1
    return count
