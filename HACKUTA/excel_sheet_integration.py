import pandas as pd  # Import pandas to work with DataFrames
import openpyxl  # Import openpyxl to ensure the Excel engine works

# Sample sales data (you will replace this with your actual sales data)
sales_data = pd.DataFrame({
    'Product': ['Phone Case', 'Wireless Earbuds'],
    'Quantity Sold': [10, 5],
    'Price per Item': [15, 50],
    'Cost per Item': [7, 30],
    'Total Revenue': [150, 250],
    'Total Profit': [80, 100]
})

# Sample investments data (you will replace this with your actual investment data)
investments_data = pd.DataFrame({
    'Investment Type': ['Advertisement', 'Shipping Costs', 'Product Purchase (Wholesaler)'],
    'Amount': [300, 100, 600]
})

# Function to export sales and investment data to an Excel sheet
def export_to_excel():
    with pd.ExcelWriter('shop_data.xlsx', engine='openpyxl') as writer:
        sales_data.to_excel(writer, sheet_name='Sales', index=False)
        investments_data.to_excel(writer, sheet_name='Investments', index=False)
        print("Data exported to Excel successfully!")

# Call the function to export data to Excel
export_to_excel()
