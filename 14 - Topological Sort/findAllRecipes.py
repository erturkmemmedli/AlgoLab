from collections import deque

class Solution:
    def findAllRecipes(self, recipes, ingredients, supplies):
        graph = {supply: [] for supply in supplies}
        in_degree = {supply: 0 for supply in supplies}

        for i, ingredientList in enumerate(ingredients):
            for ingredient in ingredientList:
                if ingredient not in graph:
                    graph[ingredient] = []
                graph[ingredient].append(recipes[i])
                in_degree[recipes[i]] = in_degree.get(recipes[i], 0) + 1

        queue = deque(supplies)
        output = []

        while queue:
            supply = queue.popleft()
            if supply in graph:
                for ingredient in graph[supply]:
                    in_degree[ingredient] -= 1
                    if in_degree[ingredient] == 0:
                        output.append(ingredient)
                        queue.append(ingredient)
        
        return output
        
# Official solution

from collections import defaultdict
from collections import Counter
class Solution:
    def findAllRecipes(self, recipes, ingredients, supplies):
        available = set(supplies)
        answer, ingredientToRecipe, inDegree = [], defaultdict(set), Counter()

        for recipe, ingredient in zip(recipes, ingredients):
            non_available = 0

            for ing in ingredient:
                if ing not in available:
                    non_available += 1
                    ingredientToRecipe[ing].add(recipe)

            if non_available == 0:
                answer.append(recipe)
            else:
                inDegree[recipe] = non_available

        for recipe in answer:
            for recipe in ingredientToRecipe.pop(recipe, set()):
                inDegree[recipe] -= 1

                if inDegree[recipe] == 0:
                    answer.append(recipe)
                    
        return answer
