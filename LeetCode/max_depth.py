def max_depth(root):
    if not root:
        return 0
    stack, h = [root], 0
    while stack:
        newroot = stack.pop()
        if newroot.left:
            stack.append(newroot.left)
        if newroot.right:
            stack.append(newroot.right)
        h = h+1
    return h