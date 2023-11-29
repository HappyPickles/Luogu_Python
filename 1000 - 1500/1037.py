# -*-coding:utf8-*-
# Author:Maxx1797


n, k = input().split()
k = int(k)
graph = {}
dirt = {}
for _ in range(k):
    l, r = input().split()
    if l not in graph:
        graph[l] = [r]
    else:
        graph[l] = graph[l] + [r]

# print(graph)
vis = [True for _ in range(10)]


def dfs(num):
    global vis
    ans = 1
    # print('输入的是' + num)
    if num in graph:
        for i in graph[num]:
            # print(i)
            # print(vis)
            if vis[int(i)]:
                vis[int(i)] = False
                ans += 1
                # print('num' + num + ' get +1 and now ans is ' + str(ans))
                if i in graph:
                    # print('haha')
                    ans += dfs(i)
    return ans


for i in range(10):
    dirt[str(i)] = dfs(str(i))
    vis = [True for _ in range(10)]
output = 1
for s in n:
    output *= dirt[s]

# print(dirt)
print(output)
