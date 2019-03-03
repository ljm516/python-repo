processed_node = []


def init_parent_dict():
    parents = {}
    parents['a'] = "start"
    parents['b'] = "start"
    parents['fin'] = None

    return parents


def init_cost_dict():
    infinity = float('inf')
    costs = {}
    costs['a'] = 5
    costs['b'] = 2
    costs['c'] = infinity
    costs['d'] = infinity
    costs['fin'] = infinity

    return costs


def init_graph_dict():
    graph = {}
    graph['start'] = {}
    graph['start']['a'] = 5
    graph['start']['b'] = 2

    graph['a'] = {}
    graph['a']['c'] = 4
    graph['a']['d'] = 2

    graph['b'] = {}
    graph['b']['a'] = 8
    graph['b']['d'] = 7

    graph['c'] = {}
    graph['c']['d'] = 6
    graph['c']['fin'] = 3

    graph['d'] = {}
    graph['d']['fin'] = 1

    graph['fin'] = {}

    return graph


def find_lowest_cost_node(costs):
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in costs:  # 遍历所有的节点
        cost = costs[node]
        # 如果当前节点的开销更低且没有处理过
        if cost < lowest_cost and node not in processed_node:
            lowest_cost = cost  # 将其视为开销最低的节点
            lowest_cost_node = node

    return lowest_cost_node


# 实现狄克斯特拉算法
if __name__ == '__main__':
    graph = init_graph_dict()
    parents = init_parent_dict()
    costs = init_cost_dict()

    print('parents: {p}'.format(p=parents))
    node = find_lowest_cost_node(costs=costs)  # 在为处理的节点中找到开销最小的节点
    while node is not None:
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors.keys():  # 遍历当前节点的所有邻居节点
            new_cost = cost + neighbors[n]
            if costs[n] > new_cost:  # 如果经当前节点到达邻居节点开销更小
                costs[n] = new_cost  # 更新该邻居节点的开销
                parents[n] = node  # 同时将该邻居节点的父节点设置为当前节点

        processed_node.append(node)  # 将当前节点标记为已经处理过
        node = find_lowest_cost_node(costs)  # 找出下一要处理的节点

    print('parents: {p}'.format(p=parents))
