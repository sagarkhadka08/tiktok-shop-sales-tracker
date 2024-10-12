import pandas as pd  # Import pandas to use DataFrame

# Create an empty DataFrame for investments data
investments_data = pd.DataFrame(columns=['Investment Type', 'Amount'])

# Function to add investment data
def add_investment(investment_type, amount):
    global investments_data
    new_investment = pd.DataFrame({
        'Investment Type': [investment_type],
        'Amount': [amount]
    })
    
    # Append the new investment to the existing DataFrame
    investments_data = pd.concat([investments_data, new_investment], ignore_index=True)
    print(f"Investment recorded: {investment_type} | Amount: ${amount}")

# Function to calculate the total investment
def calculate_total_investment():
    total_investment = investments_data['Amount'].sum()
    print(f"\nTotal Investment: ${total_investment:.2f}")

# Example of adding investment data
add_investment('Advertisement', 200)
add_investment('Shipping Costs', 50)
add_investment('Product Purchase (Wholesaler)', 500)  # Adding the cost of buying products

# Display current investments data
print("\nCurrent Investments:")
print(investments_data)

# Calculate and display the total investment
calculate_total_investment()
