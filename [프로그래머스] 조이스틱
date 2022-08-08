import re
def solution(name):
    barrier = "A"
    barrier_idx = []
    count = 0
    now_moving = len(name)-1
    
    for i in name:
        count+=min(abs(ord("A")-ord(i)), abs(ord("A")-(ord(i)-26))) # 알파벳 바꾼횟수
    if "A" not in name:
         return count+len(name)-1
    if count == 0:
        return count
    
    for i in range(len(name)):
        if name[i]=="A" and i!=0:
            barrier_length = 1
            start_idx = i
            while start_idx!=len(name)-1:
                if name[start_idx+1]=="A":
                    barrier_length+=1
                    start_idx+=1
                else:
                    break
            tmp_barrier=[i, barrier_length] #시작점과 길이
            left = len(name)-(i+barrier_length)
            right = i-1
            tmp = min(left,right)*2+max(left,right)
            if tmp < now_moving:
                now_moving = tmp
    count+=now_moving
    return count
