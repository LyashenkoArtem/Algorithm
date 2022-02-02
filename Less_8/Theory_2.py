g = [
    [0, 0, 1, 1, 9, 0, 0, 0],
    [0, 0, 9, 4, 0, 0, 5, 0],
    [0, 9, 0, 0, 3, 0, 6, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 5, 0],
    [0, 0, 7, 0, 8, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 2, 0],
]

def dij(graph, start):
    length = len(graph)
    is_valid = [False] * length
    cost = [float('inf')] * length
    parent = [-1] * length

    cost[start] = 0
    min_cost = 0

    while min_cost < float('inf'):

        is_valid[start] = True

        for i, vortex in enumerate(graph[start]):
            if vortex != 0 and not is_valid[i]: 

                if cost[i] > vortex + cost[start]:
                    cost[i] = vortex + cost[start]
                    parent[i] = start


        min_cost = float('inf')
        for i in range(length):
            if min_cost > cost[i] and not is_valid[i]:
                min_cost = cost[i]
                start = i

    return cost

s = int(input('Введите начальную точку: '))
print(dij(g, s))