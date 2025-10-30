recipes = ['bread','sandwich','burger']
ingredients = [['yeast','flour'],['bread','meat','butter'],['sandwich','meat','bread','onions']]
supplies = ['yeast','flour','meat','butter','onions']

adj = {}

for recipe, ingredient in zip(recipes,ingredients):
    for i in ingredient:
        adj[i] = adj.get(i,[])
        v = adj.get(recipe,[])
        v.append(i)
        adj[recipe] = v

prepared, cooked, response = set(), set(), []
recipe_set, supply_set = set(recipes), set(supplies)

def dfs(v: str):
    prepared.add(v)

    if v not in recipe_set and v not in supply_set:
        return

    for u in adj[v]:
        if u not in prepared:
            dfs(u)
        if u not in cooked:
            return

    if v in recipe_set:
        response.append(v)

    cooked.add(v)

for recipe in recipes:
    if not recipe in prepared:
        dfs(recipe)

print(response)
