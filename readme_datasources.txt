Origin:
- URL for Data: https://www.themealdb.com/api.php
- Documentation: no documentation available except at the URL where the data was accessed. Recipes were collected based on alphabetical
order at this link by changing the last character of the URL to each letter in the alphabet: www.themealdb.com/api/json/v1/1/search.php?f=a 

Format(s):
The data is provided in JSON format.

Access and Caching:
- The data was accessed by making HTTP requests to the Meal DB API endpoint mentioned above.
- Caching: No caching was used.

Summary of Data:
- The data consists of recipes for various meals.
- Each meal object contains the following variables:
    idMeal: Unique identifier for the meal.
    strMeal: Name of the meal.
    strCategory: Category of the meal (e.g., Dessert, Chicken).
    strArea: Area associated with the meal (e.g., British, Malaysian).
    strInstructions: Instructions for preparing the meal.
    strMealThumb: URL of an image representing the meal.
    strTags: Tags associated with the meal.
    strYoutube: URL of a YouTube video demonstrating the preparation of the meal.
    strIngredient1 to strIngredient20: Ingredients required for the meal.
    strMeasure1 to strMeasure20: Corresponding measurements for the ingredients.
- The data source contains a variety of meals from different categories and areas, with detailed instructions on how to 
prepare each meal, along with associated images, tags, and YouTube video links for further guidance.


Example:

{
  "meals": [
    {
      "idMeal": "52768",
      "strMeal": "Apple Frangipan Tart",
      "strCategory": "Dessert",
      "strArea": "British",
      "strInstructions": "Preheat the oven to 200C/180C Fan/Gas 6. ..."
      "strMealThumb": "https://www.themealdb.com/images/media/meals/wxywrq1468235067.jpg",
      "strTags": "Tart,Baking,Fruity",
      "strYoutube": "https://www.youtube.com/watch?v=rp8Slv4INLk",
      "strIngredient1": "digestive biscuits",
      "strMeasure1": "175g/6oz",
      ...
    },
    // Additional meal objects...
  ]
}

