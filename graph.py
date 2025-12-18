from collections import deque, defaultdict
import heapq

# 1. Поиск количества компонент связности в неориентированном графе с помощью DFS
def find_connected_components(graph):
    """
    Находит все компоненты связности в неориентированном графе
    graph - словарь вида {вершина: [соседи]}
    Возвращает список списков: каждый подсписок - одна компонента
    """
    visited = set()
    components = []

    def dfs(v, component):
        visited.add(v)
        component.append(v)
        for neighbor in graph.get(v, []):
            if neighbor not in visited:
                dfs(neighbor, component)

    for vertex in graph:
        if vertex not in visited:
            comp = []
            dfs(vertex, comp)
            components.append(comp)

    return components


# 2. Раскраска компонент связности (альтернативный способ)
def find_connected_components_colored(graph):
    """
    Возвращает словарь {вершина: номер_компонента}, где все вершины одной компоненты имеют одинаковый номер
    """
    visited = {}
    color = 0

    def dfs(v, color):
        visited[v] = color
        for neighbor in graph.get(v, []):
            if neighbor not in visited:
                dfs(neighbor, color)

    for vertex in graph:
        if vertex not in visited:
            color += 1
            dfs(vertex, color)

    return visited


# 3. Проверка наличия цикла в неориентированном графе
def has_cycle(graph):
    """
    Возвращает True, если в графе есть цикл
    """
    visited = set()

    def dfs(vertex, parent):
        visited.add(vertex)
        for neighbor in graph.get(vertex, []):
            if neighbor == parent:
                continue
            if neighbor in visited:
                return True
            if dfs(neighbor, vertex):
                return True
        return False

    for vertex in graph:
        if vertex not in visited:
            if dfs(vertex, None):
                return True
    return False


# 4. Проверка, является ли связный граф деревом
def is_tree(graph, start):
    """
    Граф - дерево, если он связен и не содержит циклов
    """
    if not graph:
        return True

    visited = set()
    parent_map = {start: None}
    queue = deque([start])

    while queue:
        vertex = queue.popleft()
        if vertex in visited:
            continue
        visited.add(vertex)

        for neighbor in graph.get(vertex, []):
            if neighbor not in visited:
                parent_map[neighbor] = vertex
                queue.append(neighbor)
            elif neighbor != parent_map[vertex]:
                # Найдено обратное ребро - есть цикл
                return False

    # Проверяем связность: все вершины должны быть посещены
    return len(visited) == len(graph)


# 5. Алгоритм Дейкстры - поиск кратчайших путей от заданной вершины
def dijkstra(graph, start):
    """
    Возвращает словарь {вершина: минимальное расстояние от start}
    graph - словарь вида {'A': {'B': 1, 'C': 5}}
    """
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_dist, current_vertex = heapq.heappop(priority_queue)

        if current_dist > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


# 6. Проверка двудольности графа с помощью BFS
def is_bipartite(graph):

    colors = {}

    def bfs(start):
        queue = deque([start])
        colors[start] = 1
        while queue:
            node = queue.popleft()
            for neighbor in graph.get(node, []):
                if neighbor not in colors:
                    colors[neighbor] = -colors[node]
                    queue.append(neighbor)
                elif colors[neighbor] == colors[node]:
                    return False
        return True

    for vertex in graph:
        if vertex not in colors:
            if not bfs(vertex):
                return False
    return True