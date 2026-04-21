'''
100. 最大岛屿的面积
题目描述
给定一个由 1（陆地）和 0（水）组成的矩阵，计算岛屿的最大面积。岛屿面积的计算方式为组成岛屿的陆地的总数。岛屿由水平方向或垂直方向上相邻的陆地连接而成，并且四周都是水域。你可以假设矩阵外均被水包围。
输入描述
第一行包含两个整数 N, M，表示矩阵的行数和列数。后续 N 行，每行包含 M 个数字，数字为 1 或者 0，表示岛屿的单元格。
输出描述
输出一个整数，表示岛屿的最大面积。如果不存在岛屿，则输出 0。
name:sanjin
date:2026.4.21
'''
#每个小格子的面积是1，所以只需要统计每个岛屿上小格子的个数就可以了
directions=[[0,1],[1,0],[0,-1],[-1,0]]
def dfs(grid,visited,x,y):
    global count
    for i,j in directions:
        next_x=x+i
        next_y=y+j
        if next_x<0 or next_x>len(grid) or next_y<0 or next_y > len(grid[0]):
            continue
        if not visited[next_x][next_y] and grid[next_x][next_y]==1:
            visited[next_x][next_y]=True
            count+=1
            dfs(grid,visited,next_x,next_y)
n,m=map(int,input().split())
grid=[]
for i in range(n):
    grid.append(list(map(int,input().split())))
visited=[[False] * m for _ in range(n)]
result=0
for i in range(n):
    for j in range(m):
        if grid[i][j]==1 and not visited[i][j]:
            count=1
            visited[i][j]=True
            dfs(grid,visited,i,j)
            result=max(result,count)
print(result)
