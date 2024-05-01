from DataStructure import RecipeGraph
import json

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

def print_recipes(recipes):
    print("Available recipes:")
    for i, recipe in enumerate(recipes, start=1):
        print(f"{i}. {recipe}")

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

        results = graph.bfs(ingredient)
        recipes = [recipe for recipe in results.keys() if recipe != ingredient]
        
        if not recipes:
            print("No recipes found with that ingredient.")
            continue

        print("Available recipes:")
        for i, recipe in enumerate(recipes, start=1):
            print(f"{i}. {recipe}")
            
        choice = input("Enter the number of the recipe you want to view: ")
            
        try:
            choice = int(choice)
            if 1 <= choice <= len(recipes):
                selected_recipe = recipes[choice - 1]
                print(f"\nRecipe: {selected_recipe}\n")
                
                # Fetching full recipe details
                with open(filename, "r") as file:
                    data = json.load(file)
                    for meal in data["meals"]:
                        if meal["strMeal"] == selected_recipe:
                            print(f"Ingredients:")
                            for i in range(1, 21):
                                ingredient_key = f"strIngredient{i}"
                                measure_key = f"strMeasure{i}"
                                ingredient = meal[ingredient_key]
                                measure = meal[measure_key]
                                if ingredient and measure:
                                    print(f"- {measure} {ingredient}")
                            print(f"\nFull recipe instructions:\n{meal['strInstructions']}\n")
                            print(f"Here is a video link tutorial: {meal['strYoutube']}\n")
                            break
            else:
                print("Invalid choice. Please enter a valid number.")
                
        except ValueError:
            print("Invalid input. Please enter a number.")
          
if __name__ == "__main__":
    main()
