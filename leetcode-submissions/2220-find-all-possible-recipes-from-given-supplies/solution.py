class Solution:
    def findAllRecipes(
        self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]
    ) -> List[str]:

        # Khan's Algorithm for Topological Sorting

        n = len(recipes)
        available_supplies = set(supplies)
        recipe_ingredients_map = {recipes[i]: ingredients[i] for i in range(n)}
        adj = defaultdict(set)
        can_be_made = []
        in_degree = {r: 0 for r in recipes}

        for j in range(n):
            for ingredient in ingredients[j]:
                if ingredient in in_degree:
                    in_degree[recipes[j]] += 1
                adj[ingredient].add(recipes[j])

        q = deque(
            [
                item
                for item in in_degree
                if in_degree[item] == 0
                and all(
                    supply in available_supplies
                    for supply in recipe_ingredients_map[item]
                )
            ]
        )

        while q:

            curr_recipe = q.popleft()
            available_supplies.add(curr_recipe)
            can_be_made.append(curr_recipe)

            for dependent in adj[curr_recipe]:
                in_degree[dependent] -= 1

                if in_degree[dependent] == 0 and all(
                    supply in available_supplies
                    for supply in recipe_ingredients_map[dependent]
                ):
                    q.append(dependent)

        return can_be_made

