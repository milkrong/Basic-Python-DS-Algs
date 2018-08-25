def can_cross(stones):
    """
    :type stones: List[int]
    :rtype: bool

    Given a list of stones' positions (in units) in sorted ascending order, determine if the frog is able to
    cross the river by landing on the last stone. Initially, the frog is on the first stone and assume the first
    jump must be 1 unit. If the frog's last jump was k units, then its next jump must be either k - 1, k, or k + 1
    units.
    """
    stone_set, fail = set(stones), set()
    stack = [(0, 0)]
    while stack:
        stone, jump = stack.pop()
        for j in (jump-1, jump, jump+1):
            s = stone + j
            if j > 0 and s in stone_set and (s, j) not in fail:
                if s == stones[-1]:
                    return True
                stack.append((s, j))
        fail.add((stone, jump))
    return False
