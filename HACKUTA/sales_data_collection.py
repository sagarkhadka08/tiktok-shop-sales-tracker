import pandas as pd

# Initialize an empty DataFrame to store sales data
sales_data = pd.DataFrame(columns=['Product', 'Quantity Sold', 'Price per Item', 'Cost per Item', 'Total Revenue', 'Total Profit'])

# Function to add sales data
def add_sale(product, quantity, price_per_item, cost_per_item):
    total_revenue = quantity * price_per_item
    total_profit = (price_per_item - cost_per_item) * quantity
    
    # Create a new DataFrame row to append
    new_row = pd.DataFrame({
        'Product': [product],
        'Quantity Sold': [quantity],
        'Price per Item': [price_per_item],
        'Cost per Item': [cost_per_item],
        'Total Revenue': [total_revenue],
        'Total Profit': [total_profit]
    })
    
    # Use pd.concat to append the new row to the existing DataFrame
    global sales_data
    sales_data = pd.concat([sales_data, new_row], ignore_index=True)

    print(f"Sale recorded: {product} | Quantity: {quantity} | Total Revenue: {total_revenue} | Total Profit: {total_profit}")

# Example of adding sales data
add_sale('Phone Case', 10, 15, 7)
add_sale('Wireless Earbuds', 5, 50, 30)

# Display current sales data
print(sales_data)
