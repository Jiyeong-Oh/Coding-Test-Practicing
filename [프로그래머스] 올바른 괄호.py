def solution(s):
    answer = True
    stack=[]
    for i in s:
        stack.append(i)
        if stack[-2:]==["(",")"]:
            stack.pop()
            stack.pop()
    if len(stack)!=0:
        answer = False
    return answer
