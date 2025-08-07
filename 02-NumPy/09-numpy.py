import numpy as np

# -----------------------------------------
# 🔹 1. Checking array shape
# -----------------------------------------

# Example: Monthly sales data of a single product
sales = np.array([100, 150, 200, 130, 170, 180])  # shape: (6,)
print("Monthly sales data (1D):", sales)
print("Shape:", sales.shape)  # (6,)

# -----------------------------------------
# 🔹 2. Reshaping 1D to 2D
# -----------------------------------------

# Let's assume we want to store this as 2 quarters (Q1 and Q2), each with 3 months
sales_reshaped = sales.reshape(2, 3)  # 2 rows (quarters), 3 columns (months)
print("\nSales data reshaped to quarters (2D):")
print(sales_reshaped)
print("Shape:", sales_reshaped.shape)  # (2, 3)

# -----------------------------------------
# 🔹 3. Flattening 2D to 1D again
# -----------------------------------------

sales_flat = sales_reshaped.reshape(-1)  # flatten back
print("\nFlattened sales data (1D again):", sales_flat)
print("Shape:", sales_flat.shape)  # (6,)

# -----------------------------------------
# 🔹 4. Real-world example: Broadcasting using reshape
# -----------------------------------------

# Imagine 3 products (rows) and you want to add discounts per region (columns)
# Product base prices
a = np.array([[100], [200], [300]])  # shape: (3,1)
print("\nBase prices for 3 products (shape:", a.shape, "):")
print(a)

# Discounts for 3 regions (10%, 20%, 30%)
b = np.array([10, 20, 30])  # shape: (3,)
b = b.reshape(1, -1)  # shape becomes (1, 3)
print("\nDiscounts for 3 regions (shape:", b.shape, "):")
print(b)

# Broadcasting: Each product price is added with each region discount
result = a + b
print("\nPrices after adding region-wise discounts:")
print(result)
print("Shape:", result.shape)  # (3, 3)

# This gives a matrix of shape (3 products × 3 regions)

# -----------------------------------------
# 🔚 Summary
# shape → tells you the structure (rows, columns)
# reshape → rearranges the structure without changing data
# Broadcasting → auto-expands shapes when compatible
# -----------------------------------------
