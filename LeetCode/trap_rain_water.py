class Solution:
    # @param {integer[]} height
    # @return {integer}
    def trap(self, height):
        stack, res = [], 0
        for i in range(len(height)):
            while stack and height[stack[-1]] < height[i]:
                bottom = stack[-1]
                stack.pop()
                res += 0 if not stack \
                    else ((min(height[i], height[stack[-1]]) -
                           height[bottom]) * (i - stack[-1] - 1))
            stack.append(i)
        return res