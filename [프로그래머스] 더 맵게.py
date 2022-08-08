import heapq
def solution(scoville,K):
    maximum_count = len(scoville)
    heapq.heapify(scoville)
    count = 0
    while len(scoville)>=2 and scoville[0]<K:
        most_mild = heapq.heappop(scoville)
        second_mild = heapq.heappop(scoville)
        new = most_mild+second_mild*2
        heapq.heappush(scoville, new)
        count+=1
    if scoville[0]<K:
        return -1
    return count
