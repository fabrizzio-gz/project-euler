from math import inf, isinf
from copy import deepcopy
from typing import List


def numerical_network(str_network):
    """Converts string numbers to numbers and rest to infinity (inf)"""
    num_network = []
    for row in str_network:
        new_row = []
        for str_val in row:
            if str_val == '-':
                new_row.append(inf)
            else:
                new_row.append(int(str_val))
        num_network.append(new_row)
    return num_network


def only_shortest_path(network):
    """Keeps only minimal value on each row"""
    result_network = []
    for row in network:
        new_row = []
        min_val = min(row)
        only_one = True
        for value in row:
            if value == min_val and only_one:
                new_row.append(value)
                only_one = False
            else:
                new_row.append(0)
        result_network.append(new_row)
    return result_network


def complete_paths(network):
    """Makes A->B => B->A"""
    n = len(network)
    for i in range(n):
        for j in range(i + 1, n):
            if network[i][j]:
                network[j][i] = network[i][j]
            if network[j][i]:
                network[i][j] = network[j][i]
    return network


def nodes_connected_to(node, network):
    """
    node : Int identifying a node.
    network : A matrix of n x n paths between nodes.
    Return set of all nodes connected to `node`
    """
    nodes = []
    for node_index, path in enumerate(network[node]):
        if path:
            nodes.append(node_index)
    return set(nodes)


def get_connected_nodes(connected_nodes, next_nodes, network):
    """Recursively adds connected nodes from `start` row"""
    # Get nodes from first node if none given
    if next_nodes is None:
        node = list(connected_nodes)[0]
        next_nodes = nodes_connected_to(node, network)

    # Add new nodes to connected ones
    connected_nodes = connected_nodes.union(next_nodes)

    # Get new nodes that aren't already connected
    new_nodes = set()
    for node in next_nodes:
        new_nodes = new_nodes.union(nodes_connected_to(node, network))
    new_nodes = new_nodes - connected_nodes

    if not new_nodes:
        return connected_nodes
    else:
        return get_connected_nodes(connected_nodes, new_nodes, network)


def get_all_groups(network):
    """
    Get groups of connected nodes starting from least,
    not connected node.
    """
    all_nodes = set(range(len(network)))
    groups = []
    unconnected_nodes = all_nodes
    already_connected = set()

    while len(unconnected_nodes) != 0:
        next_node = {min(unconnected_nodes)}
        group = get_connected_nodes(next_node, None, network)
        already_connected = already_connected.union(group)
        groups.append(group)
        unconnected_nodes = unconnected_nodes - already_connected

    return groups


def count_node_cycles(connected_nodes: list, nodes_to_check: set, network: List[list], cycles=0, already_verified=None) -> int:
    """
    Return number of cycles present in network, starting from a node.
    """
    if already_verified is None:
        already_verified = [False] * len(network)
        # Starting at node 0
        already_verified[0] = True
    
    node_from = connected_nodes[-1]

    for next_node in nodes_to_check:
        if next_node not in connected_nodes:
            connected_nodes.append(next_node)
            already_verified[next_node] = True
            nodes_from_next_node = nodes_connected_to(next_node, network)
            nodes_from_next_node.remove(node_from)
            cycles += count_node_cycles(connected_nodes, nodes_from_next_node, network, cycles)
        elif not already_verified[next_node]:
            cycles += 1

    return cycles


def count_group_cycles(group, network):
    """
    network : A matrix of n x n paths between nodes.
    group : A set of nodes.
    Return the number of cycles in among `group` nodes in
    `network`.
    """
    nodes = list(group)
    first_node = nodes[0]
    nodes_to_check = list(nodes_connected_to(first_node, network))
    connected_nodes = [first_node]
    return count_node_cycles(connected_nodes, nodes_to_check, network)


def get_maximum_paths(node_group, network):
    """Return all paths > 0 for nodes in `node_group`  in decreasing order"""
    maximum_paths = []
    for node in node_group:
        for path in network[node]:
            if path != 0:
                maximum_paths.append(path)
    maximum_paths = list(set(maximum_paths))
    return sorted(maximum_paths, reverse=True)


def count_path_occurrences_in_group(path, node_group, network):
    """
    Scans top diagonal part of `network`.
    Return all occurrences of `path` among nodes in `node_group`
    """
    count = 0
    for node_x in node_group:
        for node_y in range(node_x + 1, len(network)):
            if network[node_x][node_y] == path:
                count += 1
    return count





def delete_path_in(path_to_delete, node_group, network, cycle_count):
    """
    Deletes path=`path` among nodes in `node_group`
    If there is more than one occurrence of path among
    `node_group` node's, delete path that decreases cycle count
    and preserves node_group.
    Else return network with first occurrence of `path` deleted.
    """
    path_ocurrences = count_path_occurrences_in_group(path_to_delete, node_group, network)
    if  path_ocurrences >= 1:
        needs_testing = True

    for node_from in node_group:
        for node_to in range(node_from + 1, len(network)):
            path = network[node_from][node_to]
            if path == path_to_delete:
                network[node_from][node_to] == 0
                network[node_to][node_from] == 0
                if not needs_testing:
                    return network
                else:
                    path_ocurrences -= 1
                    first_node = {min(node_group)}
                    new_node_group = get_connected_nodes(first_node, None, network)
                    new_cycle_count = count_group_cycles(new_node_group, network)
                    if new_node_group == node_group and new_cycle_count < cycle_count:
                        return network
                    else:
                        if path_ocurrences == 1:
                            # Returns last possible deletion of path
                            return network
                        # Revert changes and continue trying
                        # with new path deletion
                        network[node_from][node_to] == path
                        network[node_to][node_from] == path


def minimize_group(node_group, network):
    """
    If cycles are present in node_group using network paths,
    delete the largest possible path that maintains the nodes
    connected and decreases the cycle count.
    Continue until no cycles are present.
    Return the resultant network after deleting all redundant paths.
    """
    cycle_count = count_group_cycles(node_group, network)
    if cycle_count == 0:
        return network

    first_node = {min(node_group)}
    original_network = deepcopy(network)
    maximum_paths = get_maximum_paths(node_group, network)
    for path in maximum_paths:
        network = delete_path_in(path, node_group, deepcopy(network), cycle_count)
        new_node_group = get_connected_nodes(first_node, None, network)
        new_cycle_count = count_group_cycles(new_node_group, network)
        # Verify all nodes  are still connected and cycles have decrased
        if new_node_group == node_group and new_cycle_count < cycle_count:
            # Continue minimizing in already optimized network
            return minimize_group(node_group, deepcopy(network))
        else:
            # Revert changes
            network = deepcopy(original_network)

    print("We shouldn't be here!")


def trim_groups(network, groups):
    """
    For each group, returns the minimally connected network
    by deleting redundant paths.
    """
    for node_group in groups:
        network = minimize_group(node_group, network)

    return network


def get_available_paths(network, original_network):
    """
    Return matrix of paths that were in original_network but
    aren't in network.
    """
    available_paths_network = [[0 for row in range(len(network))] for col in range(len(network))]
    for node_x in range(len(network)):
        for node_y in range(node_x + 1, len(network)):
            if original_network[node_x][node_y] and not network[node_x][node_y]:
                available_paths_network[node_x][node_y] = original_network[node_x][node_y]
                available_paths_network[node_y][node_x] = original_network[node_x][node_y]
    return available_paths_network


def flatten_and_filter(matrix):
    """Return a list of all elements != 0 in n x n matrix"""
    non_zero_vals = []
    for i in range(len(matrix)):
        # Network diagonals are always 0
        for j in range(i + 1, len(matrix)):
            if matrix[i][j]:
                non_zero_vals.append(matrix[i][j])
    return non_zero_vals


def count_path_occurrences(path, network):
    """
    Scans top diagonal part of `network`.
    Return all occurrences of `path` in network.
    """
    count = 0
    for node_x in range(len(network)):
        for node_y in range(node_x + 1, len(network)):
            if network[node_x][node_y] == path:
                count += 1
    return count


def include_path(path, network, source_network):
    """
    Will fill empty path in network with path `path` source_network
    """
    path_count = count_path_occurrences(path, source_network)
    if path_count > 1:
        print('Path between groups is present more than once')

    for node_x in range(len(network)):
        for node_y in range(node_x + 1, len(network)):
            if source_network[node_x][node_y] == path and not network[node_x][node_y]:
                network[node_x][node_y] = source_network[node_x][node_y]
                network[node_y][node_x] = source_network[node_x][node_y]
                return network
    print('Couldn t fill empty path')
    return network

def connect_groups(network, original_network, groups):
    """
    Attempts to fill all minimum paths that aren't in `network`,
    until all paths are connected.
    """
    available_paths_network = get_available_paths(network, original_network)
    min_paths = sorted(flatten_and_filter(available_paths_network))
    network_backup = deepcopy(network)
    for path in min_paths:
        network = include_path(path, network, available_paths_network)
        new_groups = get_all_groups(network)
        if len(new_groups) == 1:
            return network
        if len(new_groups) < len(groups):
            groups = new_groups
            network_backup = deepcopy(network)
        else:
            network = deepcopy(network_backup)

    print("Shouldn't reach this point!")


def inf_to_zero(matrix):
    """Return matrix where all inf vals changed to 0"""
    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            if isinf(value):
                matrix[i][j] = 0
    return matrix


def minimize(network):
    """
    Return the minimal, all nodes connected, network.
    """
    original_network = deepcopy(inf_to_zero(deepcopy(network)))
    network = only_shortest_path(network)
    network = complete_paths(network)
    groups = get_all_groups(network)
    network = trim_groups(network, groups)
    network = connect_groups(network, original_network, groups)

    return network


def get_weigth(matrix):
    """Return sum of top diagonal elements of n x n matrix"""
    total = 0
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix)):
            total += matrix[i][j]
    return total


def pp(matrix):
    for row in matrix:
        print(row)


def main():
    with open('p107_network.txt') as file:
        network_raw = file.read().splitlines()

    network = []
    for row in network_raw:
        network.append(row.split(','))

    network = numerical_network(network)
    original_network = deepcopy(inf_to_zero(deepcopy(network)))
    initial_weight = get_weigth(original_network)
    network = minimize(network)
    min_weight = get_weigth(network)
    print('Save of {}'.format(initial_weight - min_weight))
    


# # Test network
# network_raw = [['-	16	12	21	-	-	-'],
#                ['16	-	-	17	20	-	-'],
#                ['12	-	-	28	-	31	-'],
#                ['21	17	28	-	18	19	23'],
#                ['-	20	-	18	-	-	11'],
#                ['-	-	31	19	-	-	27'],
#                ['-	-	-	23	11	27	-']]

# network = []
# for row in network_raw:
#     network.append(row[0].split('\t'))

# network = numerical_network(network)
# for group in groups:
#     network = delete_cycles(network, group)
# network = connect_groups(network, groups)

# Test case
# mat = [[0, 1, 1, 1],
#        [1, 0, 1, 1],
#        [1, 1, 0, 1],
#        [1, 1, 1, 0]]
# group = {0, 1, 2, 3}
