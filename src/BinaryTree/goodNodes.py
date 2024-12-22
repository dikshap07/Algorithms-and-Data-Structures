"""
Find all good_nodes in a binary tree
good node : nodes for which the path from root to them doesnt have any node > curr node
"""


def goodNodes(root) -> int:
    if not root:
        return 0

    stack = [(root, root.val)]  # root, max_val in taht tree
    good_nodes = 0

    while stack:

        curr, max_node_val = stack.pop()

        if curr.val >= max_node_val:
            good_nodes += 1

        if curr.left:
            stack.append((curr.left, max(max_node_val, curr.val)))

        if curr.right:
            stack.append((curr.right, max(max_node_val, curr.val)))

    return good_nodes