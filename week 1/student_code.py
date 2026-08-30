def robot_navigation(nodes):
    """Validate a robot path and calculate its total weight."""
    graph = {
        "a": {"b": 1, "d": 5},
        "b": {"c": 2, "f": 5},
        "c": {"e": 1, "h": 3},
        "d": {"f": 3},
        "e": {"d": 3, "i": 2},
        "f": {"e": 4, "g": 3, "i": 3, "k": 2},
        "g": {"h": 2},
        "h": {"i": 1, "j": 2, "z": 4},
        "i": {"j": 4, "k": 2},
        "j": {"c": 1, "k": 3, "z": 4},
        "k": {"z": 3},
        "z": {}
    }
    if not isinstance(nodes, list):
        return -1

    if not nodes:
        return -1

    if not all(isinstance(node, str) for node in nodes):
        return -1

    if nodes[0] != "a":
        return -1

    if any(node not in graph for node in nodes):
        return -1

    total_weight = 0
    visited = {nodes[0]}

    for current_node, next_node in zip(nodes, nodes[1:]):
        if next_node not in graph[current_node]:
            return -1

        if next_node in visited:
            return -2

        total_weight += graph[current_node][next_node]
        visited.add(next_node)

    if nodes[-1] != "z":
        return (0, nodes[-1])

    return (total_weight, nodes[-1])