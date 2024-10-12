import pandas as pd  # Import pandas to work with DataFrames

# Load the investments data from the Excel file
investments_data = pd.read_excel('shop_data.xlsx', sheet_name='Investments')

# Load the sales data from the Excel file
sales_data = pd.read_excel('shop_data.xlsx', sheet_name='Sales')

# Function to calculate ROI
def calculate_roi():
    total_investment = investments_data['Amount'].sum()
    total_revenue = sales_data['Total Revenue'].sum()
    
    if total_investment == 0:  # Prevent division by zero
        print("Total investment is zero. ROI cannot be calculated.")
        return
    
    roi = (total_revenue - total_investment) / total_investment * 100
    print(f"Total Investment: ${total_investment:.2f}")
    print(f"Total Revenue: ${total_revenue:.2f}")
    print(f"Return on Investment (ROI): {roi:.2f}%")

# Call the function to calculate and print ROI
calculate_roi()
