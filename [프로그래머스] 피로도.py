import itertools
def solution(k, dungeons):
    nPr = list(itertools.permutations([i for i in range(len(dungeons))], len(dungeons)))
    rounding_lst = []
    for case in nPr:
        count = 0
        hp = k
        for i in case:
            if hp>= dungeons[i][0]:
                count+=1
                hp -=dungeons[i][1]
            else:
                break
        rounding_lst.append(count)
