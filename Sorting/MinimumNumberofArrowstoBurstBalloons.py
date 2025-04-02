"""
There are some spherical balloons taped onto a flat wall that represents the XY-plane. The balloons are represented as a 2D integer array points where points[i] = [xstart, xend] denotes a balloon whose horizontal diameter stretches between xstart and xend. You do not know the exact y-coordinates of the balloons.

Arrows can be shot up directly vertically (in the positive y-direction) from different points along the x-axis. A balloon with xstart and xend is burst by an arrow shot at x if xstart <= x <= xend. There is no limit to the number of arrows that can be shot. A shot arrow keeps traveling up infinitely, bursting any balloons in its path.

Given the array points, return the minimum number of arrows that must be shot to burst all balloons.
"""

# Intuition is suppoose two balloons are like
# 1--------------------------6
#           2---------------------------------8
# so we can fire between the least of the last interval of both

# One more example
# 1--------------------------6
#         2---------------------------------8
#                 3------------------------------------------10

# So these three will overlap as 6 > 2 and we will take 6 (min (8 and 6)) and then since 6 > 3 so we will still take 6 (min(6, 10))
# so for these three baloons we will require one arrow

class Solution:
    def findMinArrowShots(self, points):
        points.sort()
        res = 0

        for i in range(1, len(points)):
            if points[res][1] >= points[i][0]:
                points[res][1] = min(points[i][1], points[res][1])
            
            else:
                res += 1
                points[res] = points[i]
        
        return res+1