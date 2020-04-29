#图的BFS
def BFS(graph, start):
    queue = []
    queue.append(start)
    visited = set()
    visited.add(start)

    while queue:
        node = queue.pop()
        visited.add(node)

        process(node)
        #find next node, check next node is not visited
        nodes = generate_related_nodes(node)
        queue.push(nodes)

    #other processing work
    ...

#树的BFS
def BFS(root):
    queue = []
    queue.append(root)

    while queue:
        node = queue.pop()

        process(node)
        #find next node
        nodes = generate_related_nodes(node)
        queue.push(nodes)

    #other processing work
    ...


#递归
visited = set()
def DFS(root, visited):
    visited.add(root)
    process(node)

    for next_node in node.children():
        if not next_node in visited:
            DFS(next_node, visited)

#非递归
def DFS(root):
    if root is None:
        return []

    visited, stack = [], [root]

    while stack:
        node = statck.pop()
        visited.add(node)

        process(node)
        nodes = generate_related_nodes(node)
        stack.push(nodes)

    #other processing work
    ...
