def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount.
    If the discount is 20% or higher, apply the discount; otherwise, return the original price.
    """
    if discount_percent >= 20:
        return price - (price * discount_percent / 100)
    return price

# Get user input
price = float(input("Enter the original price: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate final price
final_price = calculate_discount(price, discount_percent)

# Print the result
print(f"Final price: {final_price:.2f}")
