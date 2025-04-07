class Solution:
    def previousSmallerElement(self, arr, n):
        res = [-1] * n
        stack = []
        for i in range(n):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            res[i] = stack[-1] if stack else -1
            stack.append(i)
        return res

    def nextSmallerElement(self, arr, n):
        res = [n] * n
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            res[i] = stack[-1] if stack else n
            stack.append(i)
        return res

    def getMaxArea(self, arr):
        n = len(arr)
        pse = self.previousSmallerElement(arr, n)
        nse = self.nextSmallerElement(arr, n)
        max_area = 0
        for i in range(n):
            width = nse[i] - pse[i] - 1
            area = arr[i] * width
            if area > max_area:
                max_area = area
        return max_area