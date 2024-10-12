import pandas as pd  # Import pandas to work with DataFrames

# Load the sales data from the Excel file
sales_data = pd.read_excel('shop_data.xlsx', sheet_name='Sales')

# Function to calculate total profit/loss
def calculate_total_profit_loss():
    total_profit = sales_data['Total Profit'].sum()
    print(f"Overall Profit/Loss: ${total_profit:.2f}")

# Call the function to calculate and print the profit/loss
calculate_total_profit_loss()
