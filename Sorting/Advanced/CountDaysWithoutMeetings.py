"""
You are given a positive integer days representing the total number of days an employee is available for work (starting from day 1). You are also given a 2D array meetings of size n where, meetings[i] = [start_i, end_i] represents the starting and ending days of meeting i (inclusive).

Return the count of days when the employee is available for work but no meetings are scheduled.

Note: The meetings may overlap.
"""

def countDays(days, meetings):
    #---------- Merges Overlapping Intervals ----------
    meetings.sort(key=lambda x: x[0])

    res = 0
    for i in range(1, len(meetings)):
        if meetings[res][1] >= meetings[i][0]:
            meetings[res][1] = max(meetings[res][1], meetings[i][1])
        else:
            res += 1
            meetings[res] = meetings[i]

    #---------- Counting Gaps ----------

    # -> In bewteen gaps
    free_days = 0
    for i in range(1, res+1):
        free_days += (meetings[i][0] - meetings[i-1][1]) - 1

    # -> Gaps before first meeting
    free_days += (meetings[0][0] - 1)

    # -> Gaps after first meeting
    free_days += (days - meetings[res][1])

    return free_days