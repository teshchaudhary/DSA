def NumberOfPathsRec(a, b):
    # If either row or column count is less than 1, it's an invalid grid, so return 0
    if a < 1 or b < 1:
        return 0

    # Base case: If we have only one row and one column, we are already at the destination
    if a == 1 and b == 1:
        return 1

    # Recursive case:
    # Move one step up (reducing row count by 1) and calculate paths
    # Move one step left (reducing column count by 1) and calculate paths
    # The total number of paths is the sum of both possibilities
    return NumberOfPathsRec(a - 1, b) + NumberOfPathsRec(a, b - 1)

def NumberOfPathsDP(a, b):
    # Initialize a 2D array (dp) of size a x b with all values set to 0.
    # dp[i][j] will represent the number of unique paths to reach cell (i, j).
    dp = [[0 for _ in range(b)] for _ in range(a)]
    
    # Fill the dp table using a nested loop for all rows and columns.
    for i in range(a):
        for j in range(b):
            # Base case: If we are in the first row or first column, there is only one way to reach each cell
            # (either move right along the row or move down along the column).
            if i == 0 or j == 0:
                dp[i][j] = 1  # Only one path is possible

            # For other cells, the number of paths is the sum of the paths from the cell above (dp[i-1][j])
            # and the paths from the cell to the left (dp[i][j-1]). (overlapped)
            else:
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    # Return the number of unique paths to the bottom-right cell (a-1, b-1).
    return dp[a - 1][b - 1]