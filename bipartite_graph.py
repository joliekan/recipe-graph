import json
from collections import defaultdict, deque

class RecipeGraph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, node1, node2):
        self.graph[node1].append(node2)

    def bfs(self, start):
        visited = set()
        queue = deque([(start, [])])
        results=defaultdict(list)
        while queue:
            node, path = queue.popleft()
            if node not in visited:
                visited.add(node)
                if start in self.graph[node]:
                    results[node]=self.graph[node]
                for neighbor in self.graph[node]:
                    if neighbor not in visited:
                        queue.append((neighbor, path + [neighbor]))
        return results
                    
    def print_graph(self):
        print(self.graph)
        
    def get_graph(self):
        return self.graph

def build_graph(filename):
    graph = RecipeGraph()
    with open(filename, "r") as file:
        data = json.load(file)
        meals = data["meals"]
        for meal in meals:
            recipe_name = meal["strMeal"]
            ingredients = [meal[f"strIngredient{i}"].lower() for i in range(1, 21) if meal[f"strIngredient{i}"]]
            
            for ingredient in ingredients:
                graph.add_edge(recipe_name, ingredient.lower())
                graph.add_edge(ingredient.lower(), recipe_name)
    
    return graph

def main():
    filename = "recipes.txt"
    graph = build_graph(filename)

    while True:
        ingredient = input("Enter an ingredient or type 'exit' to exit: ")
        if ingredient.lower() == "exit":
            break
        if ingredient.lower() not in graph.get_graph():
            print("No recipes found with that ingredient.")
            continue

        results=graph.bfs(ingredient)
        for recipe, ingredients in results.items():  # Ensure ingredient is lowercased
            if ingredients != recipe:
                print(f"Recipe: {recipe}, Ingredients: {', '.join(ingredients)}")
               
            

if __name__ == "__main__":
    main()
