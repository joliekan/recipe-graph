Recipe Finder Project Documentation

Interactions:
1. When running the program, the user is prompted to enter an ingredient or type 'exit' to exit.
2. The user then enters the name of an ingredient they want to search recipes for.
3. If the entered ingredient is found in the recipes database, the program displays the available recipes containing that ingredient.
4. The user is prompted to enter the number corresponding to the recipe they want to view.
5. The program then displays the selected recipe's name, ingredients with measurements, full recipe instructions, and a YouTube video link (if available).
6. After viewing a recipe, the program returns to step 1 unless the user chooses to exit.

Special Instructions:
- Make sure that the 'recipes.txt' file containing recipe data is in the same directory as the Python script.
- Internet connection is required to access YouTube video links.

Required Python Packages:
- None

Graph Organization:
- Nodes: Recipes and Ingredients
- Edges: Directed edges from Recipes to Ingredients and vice versa, representing the relationship between recipes and their ingredients. This allows the user to 
find several recipes that use the same ingredient, which is useful for menu planning with a limited set of ingredients. 

