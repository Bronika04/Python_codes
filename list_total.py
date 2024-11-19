# Define the price brackets
def calculate_printing_cost(pages):
    cost = 0
    # Pricing for 1 to 100 pages
    if pages <= 100:
        cost = pages * 4
    # Pricing for 101 to 200 pages
    elif pages <= 200:
        cost = (100 * 4) + (pages - 100) * 3
    # Pricing for 201 to 300 pages
    elif pages <= 300:
        cost = (100 * 4) + (100 * 3) + (pages - 200) * 2
    # Pricing for more than 300 pages
    else:
        cost = (100 * 4) + (100 * 3) + (100 * 2) + (pages - 300) * 1.5
    
    return cost

# Orders by Ram and Shyam
ram_orders = [225, 348, 765, 178, 278, 476, 78]
shyam_orders = [456, 234, 167, 98, 365]

# Calculate total cost for Ram
ram_total_cost = sum(calculate_printing_cost(order) for order in ram_orders)
# Calculate total cost for Shyam
shyam_total_cost = sum(calculate_printing_cost(order) for order in shyam_orders)

# Print the total amounts
print(f"Total cost for Ram's orders: {ram_total_cost}")
print(f"Total cost for Shyam's orders: {shyam_total_cost}")