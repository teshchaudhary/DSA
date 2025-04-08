"""
You have information about n different recipes. You are given a string array recipes and a 2D string array ingredients. The ith recipe has the name recipes[i], and you can create it if you have all the needed ingredients from ingredients[i]. A recipe can also be an ingredient for other recipes, i.e., ingredients[i] may contain a string that is in recipes.

You are also given a string array supplies containing all the ingredients that you initially have, and you have an infinite supply of all of them.

Return a list of all the recipes that you can create. You may return the answer in any order.

Note that two recipes may contain each other in their ingredients.
"""

from collections import defaultdict, deque
from typing import List

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        indegree = defaultdict(int)
        graph = defaultdict(list)
        available = set(supplies)

        for i in range(len(recipes)):
            recipe = recipes[i]
            for ingredient in ingredients[i]:
                graph[ingredient].append(recipe)
                indegree[recipe] += 1
                
        queue = deque(supplies)
        result = []

        while queue:
            item = queue.popleft()

            for neighbor in graph[item]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
                    result.append(neighbor)
                    available.add(neighbor)

        return result
