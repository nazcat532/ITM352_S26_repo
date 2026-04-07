# Application supported with Gemini (AI)
# AI assisted code for a sales data dashboard with pivot table analytics and history tracking.
# Those suggestions were reviewed and similfied by the student to meet the requirements of the assignment and to ensure clarity and maintainability.

import pandas as pd
import time
import os
import sys

# --- R1.2: EMPTY DICTIONARY FOR HISTORY ---
# This dictionary stores results. Key: String name, Value: DataFrame
analysis_history = {}

def load_sales_data():
    """
    R1. Loading sales data: Allows selection of alternate datasets, 
    tracks loading time, counts rows, and handles missing data.
    """
    print("\n" + "-"*30)
    print("FILE SELECTION")
    print("-"*30)
    print("1. sales_data.csv")
    print("2. alternate_sales_data.csv")
    
    file_choice = input("Select a dataset number (1 or 2): ").strip()
    
    # Selecting the file path based on user input
    if file_choice == "2":
        filename = "alternate_sales_data.csv"
    else:
        filename = "sales_data.csv"

    # R1: Display indicator that the file is loading
    print(f"[*] Loading data from '{filename}'...")
    start_time = time.time()
    
    # R1: Defensive programming - check if file exists before loading
    if not os.path.exists(filename):
        print(f"Error: The file '{filename}' was not found.")
        sys.exit() # End the program with an appropriate error message

    try:
        df = pd.read_csv(filename)
        # R1: Replace any missing data with zeros
        df.fillna(0, inplace=True)
        
        # R1: Display time it took to load, row count, and available columns
        load_duration = time.time() - start_time
        print(f"[SUCCESS] Successfully loaded in {load_duration:.4f} seconds.")
        print(f"Total rows: {len(df)}")
        print(f"Available columns: {list(df.columns)}")
        
        # R1: Check for required fields and warn user
        required = ['sales_region', 'order_type', 'state', 'customer_type', 'product_category', 'quantity', 'sale_price', 'employee_name']
        missing = [f for f in required if f not in df.columns]
        if missing:
            print(f"WARNING: Missing fields {missing}. Some analytics may not work.")
            
        return df, filename
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit()

def store_result(title, result_df):
    """Utility to save pivot tables into the history dictionary."""
    timestamp = time.strftime("%H:%M:%S")
    entry_name = f"[{timestamp}] {title}"
    analysis_history[entry_name] = result_df
    return result_df

# --- R3. PREDEFINED ANALYTICAL TASKS ---

def show_data_preview(df):
    """R3: Show the first n rows of sales data."""
    total_rows = len(df)
    print(f"\nEnter rows to display:")
    print(f"- Enter a number 1 to {total_rows}")
    print("- To see all rows, enter 'all'")
    print("- To skip preview, press Enter")
    
    choice = input("Your choice: ").strip().lower()
    
    if choice == "":
        return
    elif choice == 'all':
        print(df)
    elif choice.isdigit():
        n = int(choice)
        if 1 <= n <= total_rows:
            print(df.head(n))
        else:
            print(f"Invalid input. Please enter 1 to {total_rows}.")
    else:
        print("Invalid input.")

def analyze_data(choice, df):
    """Executes the specific pivot table logic based on the menu choice."""
    
    if choice == "2":
        # R3: Total sales by region and order_type
        res = df.pivot_table(values='sale_price', index='sales_region', columns='order_type', aggfunc='sum')
        print("\n--- Total Sales by Region and Order Type ---")
        print(store_result("Total Sales (Region/Order Type)", res))

    elif choice == "3":
        # R3: Average sales by region with average sales by state and sale type
        res = df.pivot_table(values='sale_price', index='sales_region', columns=['state', 'order_type'], aggfunc='mean')
        print("\n--- Average Sales Hierarchy ---")
        print(store_result("Avg Sales (Region/State/Type)", res))

    elif choice == "4":
        # R3: Sales by customer type and order type by state
        res = df.pivot_table(values='sale_price', index=['state', 'customer_type', 'order_type'], aggfunc='sum')
        print("\n--- Sales by State and Type ---")
        print(store_result("Sales (State/Cust/Order)", res))

    elif choice == "5":
        # R3: Total sales quantity and price by region and product
        res = df.pivot_table(values=['quantity', 'sale_price'], index=['sales_region', 'product_category'], aggfunc='sum')
        print("\n--- Sales Qty and Price by Region/Product ---")
        print(store_result("Qty/Price by Region/Product", res))

    elif choice == "6":
        # R3: Total sales quantity and price customer type
        res = df.pivot_table(values=['quantity', 'sale_price'], index=['order_type', 'customer_type'], aggfunc='sum')
        print("\n--- Qty and Price by Customer Type ---")
        print(store_result("Qty/Price by Customer Type", res))

    elif choice == "7":
        # R3: Max and min sales price of sales by category
        res = df.pivot_table(values='sale_price', index='product_category', aggfunc=['max', 'min'])
        print("\n--- Max/Min Sales Price by Category ---")
        print(store_result("Max/Min by Category", res))

    elif choice == "8":
        # R3: Number of unique employees by region
        res = df.pivot_table(values='employee_name', index='sales_region', aggfunc='nunique')
        print("\n--- Unique Employees by Region ---")
        print(store_result("Unique Employees Count", res))

    elif choice == "9":
        # R4: Create a custom pivot table
        print(f"\nAvailable columns: {list(df.columns)}")
        row_choice = input("Enter column(s) for Rows (comma separated): ")
        val_choice = input("Enter column for Values (numeric): ")
        
        # Simple validation: ensure column names are in the list
        if val_choice in df.columns:
            res = df.pivot_table(values=val_choice, index=row_choice.split(','), aggfunc='sum')
            print(store_result(f"Custom: {val_choice} by {row_choice}", res))
        else:
            print("Invalid column selection.")

    elif choice == "10":
        # R1.2: Display all stored results
        if not analysis_history:
            print("\nNo history recorded yet.")
        else:
            print("\n--- HISTORICAL RESULTS ---")
            for key in analysis_history:
                print(f"\n--- {key} ---")
                print(analysis_history[key])

# --- R2: INTERACTIVE COMMAND LINE MENU ---

def main():
    # R1: Initial loading of data
    sales_df, active_file = load_sales_data()
    
    while True:
        # R1.2: List analytics done so far above the menu
        print("\n" + "="*40)
        print(f"CURRENT DATASET: {active_file}")
        print(f"ANALYTICS PERFORMED: {len(analysis_history)}")
        print("="*40)
        
        print("--- Sales Data Dashboard ---")
        print("1. Show the first n rows of sales data")
        print("2. Total sales by region and order_type")
        print("3. Average sales by region/state/sale type")
        print("4. Sales by customer type/order type/state")
        print("5. Total quantity/price by region/product")
        print("6. Total quantity/price by customer type")
        print("7. Max and min sales price by category")
        print("8. Number of unique employees by region")
        print("9. Create a custom pivot table")
        print("10. Display all stored results")
        print("11. Switch / Reload Data File")
        print("12. Exit")
        
        choice = input("\nYour choice: ").strip()
        
        if choice == "12":
            print("Exiting Dashboard...")
            break
        elif choice == "11":
            sales_df, active_file = load_sales_data()
        elif choice == "1":
            show_data_preview(sales_df)
        else:
            analyze_data(choice, sales_df)

if __name__ == "__main__":
    main()