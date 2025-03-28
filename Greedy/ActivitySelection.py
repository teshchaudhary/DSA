"""
You are given a set of activities, each with a start time and a finish time, represented by the arrays start[] and finish[], respectively. A single person can perform only one activity at a time, meaning no two activities can overlap. Your task is to determine the maximum number of activities that a person can complete in a day.
"""

class Solution:
    def activitySelection(self, start, finish):
        n = len(start)
        activities = []
        
        for i in range(n):
            activities.append([start[i], finish[i]])
            
        activities.sort(key = lambda x: x[1])
        
        activity_count = 1
        
        last_finish_time = activities[0][1]
        
        for i in range(1,n):
            if activities[i][0] > last_finish_time:
                activity_count += 1
                last_finish_time = activities[i][1]
                
        return activity_count
