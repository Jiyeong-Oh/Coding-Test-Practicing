def solution(progress, speeds):
    answer=[]
    while len(progress)>0:
        progress = [progress[i]+speeds[i] for i in range(len(progress))]
        count = 0
        while len(progress)>0 and progress[0]>=100:
            progress.pop(0)
            speeds.pop(0)
            count+=1
        if count!=0:
            answer.append(count)
    return answer
