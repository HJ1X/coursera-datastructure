# python3

import sys
import threading


def height(tree, root):
    max_height = 1
    parent = root
    children = tree[parent]

    if not children:
        return 0

    for child in children:
        child_height = height(tree, child)
        max_height = max(child_height, max_height)
    
    max_height += 1
    return max_height


def compute_height(n, parents):

    nodes = [[] for i in range(n)]
    root = None

    for child_index in range(n):
        parent_index = parents[child_index]
        if parent_index == -1:
            root = child_index
        else:
            nodes[parent_index].append(child_index)

    max_height = height(nodes, root)
    return max_height

    # Naive approach

    # max_height = 0
    # for vertex in range(n):
    #     height = 0
    #     current = vertex
    #     while current != -1:
    #         height += 1
    #         current = parents[current]
    #     max_height = max(max_height, height)
    # return max_height


def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height(n, parents))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()