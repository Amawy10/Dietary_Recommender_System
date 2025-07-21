# Dietary Recommender System (Python + SQL)

This project recommends fast food menu items based on user-defined dietary preferences — specifically **low-carb** and **high-protein** needs. It is especially helpful for users managing weight or diabetes-friendly diets.

## Features

- Loads a real-world fast food nutrition dataset
- Converts it into a SQLite database
- Accepts user input for **carb** and **protein** thresholds
- Returns menu items that match the user's dietary goals
- Gracefully handles cases when no food items match

## Tools & Technologies

- Python (pandas, sqlite3)
- SQLite
- CSV file input
- SQL filtering logic

## Dataset

`fastfood.csv` includes nutritional information such as:
- Calories
- Total fat
- Total carbs
- Protein
- Sodium
- Menu item names

## How It Works

1. Load the CSV into a SQLite database.
2. Ask the user for their carb/protein preferences.
3. Query the database for matching items.
4. Print the results (or a message if no matches found).

## Sample Output

```bash
Enter your maximum total carbs: 50  
Enter your minimum protein: 20  

               item_name                         total_carb  protein  calories
0  Double Cheeseburger (Wendy's)                     34         25       400
1      Grilled Chicken Sandwich (Chick-fil-A)        36         29       320
2           Chipotle Chicken Bowl                    42         34       460
