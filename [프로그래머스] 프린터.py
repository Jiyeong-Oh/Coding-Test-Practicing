def solution(priorities, location):
    printer = [i for i in range(len(priorities))]
    answer = 0
    
    while (location in printer)==True:
        tmp = priorities.pop(0)
        if len(set(priorities)-set(range(tmp+1)))==0:
#             print("중요도 더 높은 요소 없음. 인쇄해도됨")
            answer+=1
            printer.pop(0)            
        else:
#             print("있음. 뒤로 보내야함")
            priorities.append(tmp)
            indice = printer.pop(0)
            printer.append(indice)

    return answer
