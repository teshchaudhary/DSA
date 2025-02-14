# You are given heights of consecutive buildings. You can move from the roof of a building to the roof of next adjacent building. You need to find the maximum number of consecutive steps you can put forward such that you gain an increase in altitude with each step.

def maxStep(A, N):
    res = 0
    curr = 0
    for i in range(1, N):
        if A[i-1] < A[i]:
            curr += 1

        else:
            curr = 0

        res = max(res, curr)

    return res
