stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 2700,
    "MSFT": 300,
    "AMZN": 3300
}
total_investment = 0

print("📊 Stock Portfolio Tracker")
n = int(input("How many stocks do you have? "))

for i in range(n):
    stock_name = input("Enter stock name: ").upper()
    quantity = int(input("Enter quantity: "))

    # Step 5: Check if stock exists in dictionary
    if stock_name in stock_prices:
        price = stock_prices[stock_name]
        investment = price * quantity
        total_investment += investment

        print(stock_name, "->", quantity, "×", price, "=", investment)
    else:
        print("❌ Stock not found!")

print("\n Total Investment Value =", total_investment)
save = input("Do you want to save result? (yes/no): ").lower()

if save == "yes":
    file = open("portfolio.txt", "w")
    file.write("Total Investment Value = " + str(total_investment))
    file.close()
    print("✅ Saved to portfolio.txt")