'''
98. 可达路径
题目描述
给定一个有 n 个节点的有向无环图，节点编号从 1 到 n。请编写一个函数，找出并返回所有从节点 1 到节点 n 的路径。每条路径应以节点编号的列表形式表示。
输入描述
第一行包含两个整数 N，M，表示图中拥有 N 个节点，M 条边
后续 M 行，每行包含两个整数 s 和 t，表示图中的 s 节点与 t 节点中有一条路径
输出描述
输出所有的可达路径，路径中所有节点之间空格隔开，每条路径独占一行，存在多条路径，路径输出的顺序可任意。如果不存在任何一条路径，则输出 -1。
注意输出的序列中，最后一个节点后面没有空格！ 例如正确的答案是 `1 3 5`,而不是 `1 3 5 `， 5后面没有空格！
'''

def dfs(graph, x,n,path,result):
    if x == n:
        result.append(path.copy())
        return
    for i in range(1,n+1):
        if graph[x][i] == 1:
            path.append(i)
            dfs(graph,i,n,path,result)
            path.pop()
def main():
    n,m=map(int,input().split())
    graph=[[0]*(n+1) for _ in range(n+1)]
    for _ in range(m):
        s,t=map(int,input().split())
        graph[s][t]=1
    result=[]
    dfs(graph,1,n,[1],result)
    if not result:
        print(-1)
    else:
        for path in result:
            print(' '.join(map(str,path)))
if __name__ == "__main__":
    main()