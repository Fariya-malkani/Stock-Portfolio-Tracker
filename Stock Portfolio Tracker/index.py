# Simple Stock Portfolio Tracker

# Hardcoded stock prices (you can change or add more)
STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "MSFT": 320,
    "AMZN": 130
}

def main():
    print("=== Simple Stock Portfolio Tracker ===")
    print("Available Stocks:", ", ".join(STOCK_PRICES.keys()))
    print("Type 'done' when finished.\n")

    portfolio = {}
    while True:
        stock = input("Enter stock symbol (AAPL, TSLA, etc.): ").upper().strip()
        if stock == "DONE":
            break
        if stock not in STOCK_PRICES:
            print("❌ Stock not found in list. Try again.\n")
            continue

        try:
            quantity = int(input(f"Enter quantity of {stock}: "))
        except ValueError:
            print("❌ Please enter a valid number.\n")
            continue

        portfolio[stock] = portfolio.get(stock, 0) + quantity

    # Calculate total investment
    total_investment = 0
    print("\n--- Portfolio Summary ---")
    for stock, qty in portfolio.items():
        price = STOCK_PRICES[stock]
        investment = price * qty
        total_investment += investment
        print(f"{stock}: {qty} shares × ${price} = ${investment}")

    print(f"\n💰 Total Investment Value: ${total_investment}")

    # Ask to save results
    save = input("\nDo you want to save results to a file? (yes/no): ").lower().strip()
    if save == "yes":
        with open("portfolio.txt", "w") as file:
            file.write("Stock,Quantity,Price,Total\n")
            for stock, qty in portfolio.items():
                file.write(f"{stock},{qty},{STOCK_PRICES[stock]},{STOCK_PRICES[stock]*qty}\n")
            file.write(f"\nTotal Investment: ${total_investment}\n")
        print("✅ Portfolio saved to 'portfolio.txt'")

if __name__ == "__main__":
    main()
