class Node:
    def __init__(self, value):
        self.value = value
        self.in_degree = 0
        self.children = []
        self.parents = []

    def __repr__(self):
        return str(self.value)


def build_order(project_list, deps_list):
    build_list = []
    nodes_dict = {}
    # convert string representation of project to nodes
    for project in project_list:
        nodes_dict[project] = Node(project)
    # convert string representation of dependencies to edges between nodes
    # increment in-degree of all dependent nodes by 1
    for dep in deps_list:
        nodes_dict[dep[0]].children.append(nodes_dict[dep[1]])
        nodes_dict[dep[1]].parents.append(nodes_dict[dep[0]])
        nodes_dict[dep[1]].in_degree += 1
    # Kahn's algorithm for topological sorting
    # enqueue values if in-degree is 0
    q = []
    for value in project_list:
        node = nodes_dict[value]
        if node.in_degree == 0:
            build_list.append(node.value)
            q.append(node)
    # reduce child node in-degree by 1. if in-degree == 0 add to build and enqueue.
    while len(q) > 0:
        current = q.pop(0)
        for child_node in current.children:
            child_node.in_degree -= 1  # reduce in degree once parent is removed from queue
            if child_node.in_degree == 0:  # check if in_degree is 0
                build_list.append(child_node.value)
                q.append(child_node)

    if len(build_list) != len(project_list):
        return None
    return build_list


project_list = ['a', 'b', 'c', 'd', 'e', 'f']
deps_list = [('a', 'd'), ('f', 'b'), ('b', 'd'), ('f', 'a'), ('d', 'c')]

result = build_order(project_list, deps_list)
print(result)
