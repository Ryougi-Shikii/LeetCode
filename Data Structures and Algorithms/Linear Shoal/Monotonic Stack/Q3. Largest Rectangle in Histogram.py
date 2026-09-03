class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        n = len(heights)
        rightMin = [n] * n
        stack = []

        for index, currentHeight in enumerate(heights):
            while stack and currentHeight < heights[stack[-1]]:
                prevIndex = stack.pop()
                rightMin[prevIndex] = index
            stack.append(index)

        leftMin = [-1] * n
        stack.clear()
        for index in range(n-1, -1, -1):
            currentHeight = heights[index]
            while stack and currentHeight < heights[stack[-1]]:
                prevIndex = stack.pop()
                leftMin[prevIndex] = index
            stack.append(index)

        maximumArea = 0
        for i in range(n):
            maximumArea = max((rightMin[i] - leftMin[i] - 1) * heights[i], maximumArea)

        return maximumArea