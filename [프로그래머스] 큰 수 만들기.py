def solution(number, k):
    answer = ""
    chance = k
    stack = []
    
    for k in range(len(number)):
        while len(stack)>0 and number[k] > stack[-1] and chance>0:
            stack.pop()
            chance-=1
        stack.append(number[k])

    return ''.join(stack[:len(stack)-chance])
