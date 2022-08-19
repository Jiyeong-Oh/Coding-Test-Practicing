from itertools import combinations
import collections

def solution(orders, course):
    answer = []
    orders = [sorted(list(x)) for x in orders]
#     print(orders)
    for length in course:
#         print("#######################")
        menu = []
        for transaction in orders:
            menu+=list(combinations(transaction, length))
        menu = dict(collections.Counter(menu))
#         print(menu)
        menu = dict(filter(lambda x: x[1]>=2, menu.items()))
#         print(menu)
        if len(menu)>=1:
            maximum = max(menu.values())
            menu = dict(filter(lambda x: x[1]==maximum, menu.items()))
            answer+=list(menu.keys())
    for i in range(len(answer)):
        answer[i] = "".join(answer[i])
    return sorted(answer)
