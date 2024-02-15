def leaf_node():
    import sys
    from collections import deque

    input = sys.stdin.readline

    n = int(input())
    tree = list(map(int, input().split()))
    index = int(input())

    q_tree = deque()
    visited =[False] * n
    leaf_nodes = 0
    # print(q_tree)

    if tree[index] == -1:
        return 0
    else:
        tree[index] = -2
        root_node = tree.index(-1)
        # print(root_node, tree[root_node])
        deque.append(q_tree, root_node)
        while q_tree:
            node = q_tree.popleft()
            # print(f"popleft {node}")
            visited[node] = True
            will_visit = 0
            for i in range(len(tree)):
                if tree[i] == node and visited[i] is False:
                    deque.append(q_tree, i)
                    # print(f"q_tree appends {i}")
                    will_visit += 1
            # print(f"node: {node} will_visit: {will_visit}")
            if will_visit == 0:
                leaf_nodes += 1

        return leaf_nodes

print(leaf_node())