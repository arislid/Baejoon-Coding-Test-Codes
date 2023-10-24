import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

def dijkstra_fast():
    node, edge = map(int, input().split())
    start = int(input())
    
    graph = [[] for i in range(node+1)]
    distance_table = [INF] * (node + 1)
    
    for _ in range(edge):
        node_a, node_b, distance = map(int, input().split())
        graph[node_a].append((node_b, distance))
        
    q = []
    
    heapq.heappush(q, (0, start))
    distance_table[start] = 0
    
    while q:
        dist, now = heapq.heappop(q)
        if distance_table[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance_table[i[0]]:
                distance_table[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
                
    
    for i in range(1, node + 1):
        if distance_table[i] == INF:
            print("INF")
        else:
            print(distance_table[i])
            
dijkstra_fast()
