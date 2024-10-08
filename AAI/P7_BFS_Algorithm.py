import collections

def bfs(graph, root):
    visited, queue = set(), collections.deque([root])
    visited.add(root)  # Corrected the spelling from 'visisted' to 'visited'

    while queue:
        vertex = queue.popleft()
        print(str(vertex) + " ", end="")

        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)  # Changed from 'append' to 'add' since 'visited' is a set
                queue.append(neighbour)

if __name__ == "__main__":
    graph = {0: [1, 2], 1: [2], 2: [3], 3: [1, 2]}
    print("Following is Breadth First Traversal (starting from vertex 2)")
    bfs(graph, 0)
