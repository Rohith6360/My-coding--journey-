# --- Day 1: Stock Profit Calculator ---
buy_price = float(input("Enter purchase price: "))
sell_price = float(input("Enter selling price: "))
quantity = float(input("Enter number of shares: "))

profit_or_loss = (sell_price - buy_price) * quantity

print("Result: ", profit_or_loss)
