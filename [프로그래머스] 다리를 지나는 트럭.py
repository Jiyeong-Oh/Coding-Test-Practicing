def solution(bridge_length, weight, truck_weights):
    time = 0
    done = []
    ing = []
    finish = len(truck_weights)
    departing_time=[0 for i in range(len(truck_weights))]
    
    while len(done)!=finish:
        # print("time: ",time)
        # print("departing_time: ",departing_time)
        # print("state: ",done, ing, truck_weights)
        # print("################################")
        time+=1
        
        if time == departing_time[0]+bridge_length:            
            arrived = ing.pop(0)
            departing_time.pop(0)
            done.append(arrived)
            
        # 새로운 트럭이 출발 ()
        if len(truck_weights)>0 and truck_weights[0]+sum(ing)<=weight and len(ing)+1 <= bridge_length:
            now = len(departing_time)-len(truck_weights)
            departing_time[now] = time # 출발시간 캡쳐
            depart = truck_weights.pop(0) # 출발시키기
            ing.append(depart)
        
    return time
