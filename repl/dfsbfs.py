

graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D", "G"],
    "D": ["B", "C", "A"],
    "E": ["F"],
    "F": ["E"],
    "G": ["H"],
    "H": ["B", "E"]
}

def breadth_first_search(graph, start):
    ## from the start, print out all nodeds in a breadth-first traversal
  queue = []
  visited = set()

  queue.append(start)

  while len(queue) > 0:
    ##queue .0 takes "a" out of the loop
    current_node = queue.pop(0)
    print(current_node)
    visited.add(current_node)
    neighbors = graph[current_node]
    if len(neighbors) > 0:
      for neighbor in neighbors:
        if neighbor not in visited:
          queue.append(neighbor)

print("BFS: ")
breadth_first_search(graph, "A")

def depth_first_search(graph, start):
  visited = set()
  def dfs(current_node):
    neighbors = graph[current_node]
    for neighbor in neighbors:
      if neighbor not in visited:
        visited.add(neighbor)
        dfs(neighbor)
  dfs(start)

print("DFS: ")
depth_first_search(graph, "A")

