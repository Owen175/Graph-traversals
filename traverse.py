# Depth First
graph = {"A": ["B", "C", "D"], "B": ["A", "C", "E"], "C": ["A", "B"], "D": ["A"], "E": ["B", "F"], "F": ["E"]}

def depth_first(graph):
    discovered = []
    stack = []
    node = "A"
    explored = False
    x = True
    while x:
        connected = graph[node]
        old_node = node
        explored = True
        for conn in connected:
            if conn not in discovered:
                explored = False
                node = conn
                break
        if explored:
            if len(stack) == 0:
                x = False
            else:
                node = stack.pop()
        else:
            stack.append(old_node)
        if old_node not in discovered:
            discovered.append(old_node)
            
    return discovered

def breadth_first(graph):
    discovered = []
    queue = ["A"]
    while len(queue) != 0:
        node = queue.pop(0)
        discovered.append(node)
        for conn in graph[node]:
            if conn not in discovered:
                queue.append(conn)
    return discovered

breadth_first(graph)
        
    
    

print(depth_first(graph))

