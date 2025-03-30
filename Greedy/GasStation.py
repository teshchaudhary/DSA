"""
There are some gas stations along a circular route. You are given two integer arrays gas[] denoted as the amount of gas present at each station and cost[] denoted as the cost of travelling to the next station. You have a car with an unlimited gas tank. You begin the journey with an empty tank from one of the gas stations. Return the index of the starting gas station if it's possible to travel around the circuit without running out of gas at any station in a clockwise direction. If there is no such starting station exists, return -1.
Note: If a solution exists, it is guaranteed to be unique.
"""


class Solution:
    def startStation(self, gas, cost):
        n = len(gas)
        res = 0
        total_gas, current_gas = 0, 0
        
        for i in range(n):
            # If summation(gas[i] - cost[i]) < 0, it basically means it is not possible
            total_gas += gas[i] - cost[i]
            current_gas += gas[i] - cost[i]
            
            # If current_gas becomes negative, it means there is no source till i from where we can start. Why?
            # if we are at i and gas became -ve it means none of the station could possibly help to reach till i
            # so we need to make source as i + 1 (it may work or not and for that check we have out total_gas that checks if it is possible)
            if current_gas < 0:
                current_gas = 0
                res = i+1
        
        return res if total_gas >= 0 else -1