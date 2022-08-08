import itertools
def solution(numbers):
    lst = []
    answer = []
    cards = list(numbers)
    tmp = []
    for i in range(1,len(cards)+1):
        tmp+=list(itertools.permutations(cards, i))
    cards = tmp
    for i in cards:
        lst.append(int("".join(list(i))))
    lst = list(set(lst))
    for i in lst:
        state = True
        if i<2:
            state = False
        for j in range(2,i//2+1):
            if i%j==0:
                state = False
                break
        if state == True:
            answer.append(i)    
    return len(answer)
