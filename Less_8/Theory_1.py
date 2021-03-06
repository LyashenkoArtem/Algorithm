from collections import deque

g = [
    [0, 1, 1, 0, 1, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [1, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 1, 1],
    [0, 0, 0, 0, 1, 1, 0, 1],
    [0, 0, 0, 0, 0, 1, 1, 0],
]

def bfs(graph, start, finish):
    parent = [None for _ in range(len(graph))]
    is_valid = [False for _ in range(len(graph))]

    deq = deque([start])
    is_valid[start] = True

    while len(deq) > 0:

        current = deq.pop()

        if current == finish:
            # return parent
            break

        for i, vertex in enumerate(graph[current]):
            if vertex == 1 and not is_valid[i]:

                is_valid[i] = True
                parent[i] = current
                deq.appendleft(i)

    else:
        return f'Из вершины {start} нельзя попасть в вершину {finish}'
    cost = 0
    way = deque([finish])
    i = finish

    while parent[i] != start:
        cost += 1
        way.appendleft(parent[i])
        i = parent[i]

    cost += 1
    way.appendleft(start)

    return f'Путь {list(way)}, длинной в {cost}'

s = int(input('С какой вершины начинаем? '))
f = int(input('В какую идем? '))
print(bfs(g, s, f))