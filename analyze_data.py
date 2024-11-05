from pymongo import MongoClient
from pprint import pprint

# Connect to MongoDB
connection_string = 'mongodb+srv://indralathamallika2:mallika123@cluster0.d6i34.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'
client = MongoClient(connection_string)
db = client['sales_data']  # Use the same database name you used in import_csv.py
collection = db['product']  # Use the same collection name you used in import_csv.py

# Find the most sold products
most_sold_products = collection.aggregate([
    {"$group": {"_id": "$Product", "total_sold": {"$sum": "$Quantity"}}},  # Use the header 'Product' and 'Quantity'
    {"$sort": {"total_sold": -1}},
    {"$limit": 5}  # Get top 5 products
])

print("Most Sold Products:")
pprint(list(most_sold_products))

# Find the most used payment method
most_used_payment_method = collection.aggregate([
    {"$group": {"_id": "$Payment_Method", "count": {"$sum": 1}}},  # Use 'Payment_Method' header
    {"$sort": {"count": -1}},
    {"$limit": 1}  # Get the most used payment method
])

print("\nMost Used Payment Method:")
pprint(list(most_used_payment_method))

# Find the most profitable product category
most_profitable_category = collection.aggregate([
    {"$group": {"_id": "$Category", "total_profit": {"$sum": "$Total_Price"}}},  # Use 'Category' and 'Total_Price' headers
    {"$sort": {"total_profit": -1}},
    {"$limit": 1}  # Get the most profitable category
])

print("\nMost Profitable Product Category:")
pprint(list(most_profitable_category))
