def maxDepth( root) -> int:

    if not root:
        return 0

    depth = 1

    for child in root.children:

        depth = max(depth,1+maxDepth(child))

    return depth