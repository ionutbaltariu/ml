from typing import List
from collections import deque


def bfs(adj_list: List[List[int]], start_node=0):
    queue = deque()
    explored = set()
    bfs_order = []

    queue.append(start_node)

    while queue:
        popped = queue.popleft()

        if popped in explored:
            continue

        bfs_order.append(popped)
        explored.add(popped)

        for neighbour in adj_list[popped]:
            if neighbour not in explored:
                queue.append(neighbour)

    return bfs_order


print(bfs([[1, 4], [2], [3], [], []]))
