import pandas as pd
import sqlite3

#loading the dataset
data_path = 'fastfood.csv'
fast_food_data = pd.read_csv(data_path)

#connecting the SQLite database
conn = sqlite3.connect ('fastfood.db')

# Load data into SQL table
fast_food_data.to_sql ('nutritional_info', conn, if_exists='replace', index=False)

# Verify that the data was loaded successfully
print("Data loaded successfully: ")
print(pd.read_sql_query("SELECT * FROM nutritional_info LIMIT 5", conn))


conn.close()

# Function to get items with lower carbs than the specified threshold
def get_low_carb_items(conn, carb_threshold=50):
    #SQL query to select items 
    query = f"SELECT * FROM nutritional_info WHERE total_carb < {carb_threshold}"
    #Executing the query and returning the result
    return pd.read_sql_query(query, conn)
#Function to get items with higher protein than the specified threshold
def get_high_protein_items(conn, protein_threshold=20):
    #SQL query to select items
    query = f"SELECT * FROM nutritional_info WHERE protein >= {protein_threshold}"
    #Executing the query
    return pd.read_sql_query(query, conn)

#Function to get recommended items based on low carbs and high protein
def get_recommendations (conn, carb_threshold=50, protein_threshold=20):
    #SQL query to select items that meeth both conditions:
    #total carbs less than the specified threshold and portein greater than the threshhold
    query = f"""
    SELECT * FROM nutritional_info 
    WHERE total_carb < {carb_threshold} AND protein >= {protein_threshold}
    """
    return pd.read_sql_query(query,conn)

#Function to get recommendations and tell you when no items match the criteria
def recommend_menu_items(conn, carb_threshold=50, protein_threshold=20):
    recommendations = get_recommendations (conn, carb_threshold, protein_threshold)
    # Check if the recommendations DataFrame is empty
    if recommendations.empty:

        return "No items match your dietary preference"
    
    return recommendations

def get_user_preference():
    #Prompt the user to enter thei maximum carb intake and convert it to an integer
    carb_threshold = int (input("Enter your maximum total carbs: "))
    protein_threshold = int (input("Enter your maximum protein: "))

    return carb_threshold,protein_threshold

def main():

    conn = sqlite3.connect('fastfood.db')
    #get user preference
    carb_threshold, protein_threshold = get_user_preference()
    #get recommendations based on user preference
    recommendations = recommend_menu_items(conn, carb_threshold, protein_threshold)
    #print the recommendations
    print(recommendations)

if __name__=="__main__":
    main()
    