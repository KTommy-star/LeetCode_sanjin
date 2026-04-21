from collections import deque
directions=[[0,1],[1,0],[0,-1],[-1,0]]
def bfs(grid,visited,x,y):
    queue=deque([])
    queue.append([x,y])
    while queue:
        x,y=queue.pop(0)
        for i ,j in directions:
            next_x=i
            next_y=j
            if next_x < 0 or next_x > len(grid) or next_y < 0 or next_y > len(grid[0]):
                continue
            if not visited[next_x][next_y] and grid[next_x][next_y]==1:
                visited[next_x][next_y]=True
                queue.append([next_x,next_y])

def main():
    n,m=map(int,input().split())
    grid=[]
    for i in range(n):
        grid.append(list(map(int,input().split())))
    visited=[[False]*m for _ in range(n)]
    result=0
    for i in range(n):
        for j in range(m):
            if grid[i][j]==1 and not visited[i][j]:
                result+=1
                visited[i][j]=True
                bfs(grid,visited,i,j)
    print(result)

if __name__ == "__main__":
    main()