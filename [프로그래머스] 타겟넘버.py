def solution(numbers, target):
    answer=[0]
    def dfs(indice, total):
#         print(indice, total)
        if indice == len(numbers):
            if total == target:
                answer[0]+=1
#             print("switch")
            return
        dfs(indice+1, total+numbers[indice])
        dfs(indice+1, total-numbers[indice])
    dfs(0,0)
    return answer[0]
