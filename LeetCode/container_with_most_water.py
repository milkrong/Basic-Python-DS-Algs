def max_area(height):
    """
    Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical
    lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together
    with x-axis forms a container, such that the container contains the most water.
    :param height: list
    :return: int
    """
    left = 0
    right = len(height) - 1
    max_area = 0

    while left < right:
        area = (right - left) * min(height[left], height[right])
        max_area = max(area, max_area)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_area
