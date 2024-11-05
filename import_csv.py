import pandas as pd
from pymongo import MongoClient

# Connect to MongoDB
connection_string = 'mongodb+srv://indralathamallika2:mallika123@cluster0.d6i34.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'  # Replace with your actual connection string
client = MongoClient(connection_string)
db = client['sales_data']  # Replace with your database name
collection = db['product']  # Replace with your collection name

# Load CSV file into a DataFrame
df = pd.read_csv('C:/Users/User/Desktop/Assignment/e_commerce_data.csv')  # Replace with the path to your CSV file

# Convert DataFrame to dictionary and insert into MongoDB
collection.insert_many(df.to_dict('records'))
print("Data imported successfully.")

