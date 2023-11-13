from typing import List
from collections import deque


def dfs(adj_list: List[List[int]], start_node = 0):
    stack = deque()
    explored = set()
    dfs_order = []

    stack.append(start_node)

    while stack:
        popped = stack.pop()

        if popped in explored:
            continue

        dfs_order.append(popped)
        explored.add(popped)

        for neighbour in adj_list[popped]:
            if neighbour not in explored:
                stack.append(neighbour)

    return dfs_order


print(dfs([[1, 4], [2], [3], [], []]))
