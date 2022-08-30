def solution(board, c):
    queue=[]
    lst=[]
    n = len(board)
    m = len(board[0])
    start=[]
    end=[]
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j]==2:
                start=[i,j,0,1] # 좌표, 장애물 수, 길 수
                break
            elif board[i][j]==3:
                end=[i,j]
                break
    
    queue.append(start) # 시작점
    board[start[0]][start[1]]=-1 # 방문
    
    
    while queue:
        print(queue)
        now = queue.pop(0)
        if now[:2] == end: #도착했을 때
            lst.append(now)
            continue
        dong = [now[0],now[1]+1,now[2],now[2]+1]
        seo = [now[0],now[1]-1,now[2],now[2]+1]
        nam = [now[0]+1,now[1],now[2],now[2]+1]
        book = [now[0]-1,now[1],now[2],now[2]+1]
        
        if dong[1]<m and board[dong[0]][dong[1]]!=-1:
            queue.append(dong)
            if board[dong[0]][dong[1]]==1:
                dong[2]+=1
            board[dong[0]][dong[1]]=-1
        if seo[1]>=0 and board[seo[0]][seo[1]]!=-1:
            queue.append(seo)
            if board[seo[0]][seo[1]]==1:
                seo[2]+=1
            board[seo[0]][seo[1]]=-1
        if nam[0]<n and board[nam[0]][nam[1]]!=-1:
            queue.append(nam)
            if board[nam[0]][nam[1]]==1:
                nam[2]+=1
            board[nam[0]][nam[1]]=-1
        if book[0]>=0 and board[book[0]][book[1]]!=-1:
            queue.append(book)
            if board[book[0]][book[1]]==1:
                book[2]+=1
            board[book[0]][book[1]]=-1
    return lst
