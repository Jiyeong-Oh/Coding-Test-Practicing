def solution(prices):
    rising_count = [0 for i in prices]
    stack = []
    for i in range(len(prices)):
#         print(prices[i])
        while stack and stack[-1][1]>prices[i]:
            tmp = stack.pop()
            rising_count[tmp[0]]=i-tmp[0]
        stack.append([i,prices[i]])
    for i, _ in stack:
        rising_count[i] = len(prices)-i-1
#     print(rising_count)
    return rising_count
