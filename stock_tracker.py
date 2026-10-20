"""
CodeAlpha Internship - Task 2
Stock Portfolio Tracker (beginner level)

Concepts used: dictionary, input/output, basic arithmetic, file handling.
No external libraries or APIs are used - all prices are hardcoded.
"""

# ---------------------------------------------------------------
# 1. HARDCODED STOCK PRICES (dictionary)
# ---------------------------------------------------------------
# Key   = stock symbol (string)
# Value = price per share (number)

STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "MSFT": 410,
    "GOOGL": 140,
    "AMZN": 175,
    "INFY": 18,
    "TCS": 45
}


# ---------------------------------------------------------------
# 2. HELPER FUNCTIONS
# ---------------------------------------------------------------

def show_available_stocks():
    """Print every stock the tracker knows about, with its price."""
    print("\nAvailable stocks and prices (USD):")
    print("-" * 34)
    for symbol in STOCK_PRICES:
        print("  " + symbol.ljust(8) + "$" + str(STOCK_PRICES[symbol]))
    print("-" * 34)


def get_stock_symbol():
    """
    Ask for a stock symbol until a valid one is typed.
    Returns the symbol in uppercase, or 'DONE' to stop entering.
    """
    while True:
        symbol = input("\nEnter stock symbol (or type 'done' to finish): ").strip().upper()

        if symbol == "DONE":
            return "DONE"
        elif symbol == "":
            print("You typed nothing. Please enter a stock symbol.")
        elif symbol not in STOCK_PRICES:
            print("'" + symbol + "' is not in our price list. Please choose from the list above.")
        else:
            return symbol


def get_quantity(symbol):
    """Ask for a whole number of shares greater than zero."""
    while True:
        entered = input("Enter quantity of " + symbol + " shares: ").strip()

        if not entered.isdigit():
            print("Please enter a whole number (for example 10).")
        elif int(entered) == 0:
            print("Quantity must be greater than zero.")
        else:
            return int(entered)


def build_portfolio():
    """
    Collect the user's holdings into a dictionary.
    Example result: {"AAPL": 10, "TSLA": 5}
    """
    portfolio = {}

    while True:
        symbol = get_stock_symbol()

        if symbol == "DONE":
            break

        quantity = get_quantity(symbol)

        # If the same stock is entered twice, add to the existing quantity
        # instead of overwriting it.
        if symbol in portfolio:
            portfolio[symbol] = portfolio[symbol] + quantity
            print("Updated: you now hold " + str(portfolio[symbol]) + " shares of " + symbol + ".")
        else:
            portfolio[symbol] = quantity
            print("Added: " + str(quantity) + " shares of " + symbol + ".")

    return portfolio


def calculate_total(portfolio):
    """Multiply quantity by price for each stock and add it all up."""
    total = 0
    for symbol in portfolio:
        total = total + (portfolio[symbol] * STOCK_PRICES[symbol])
    return total


def display_portfolio(portfolio, total):
    """Print a neat table of the holdings and the grand total."""
    print("\n" + "=" * 50)
    print("             YOUR STOCK PORTFOLIO")
    print("=" * 50)
    print("STOCK".ljust(10) + "QTY".ljust(8) + "PRICE".ljust(12) + "VALUE")
    print("-" * 50)

    for symbol in portfolio:
        quantity = portfolio[symbol]
        price = STOCK_PRICES[symbol]
        value = quantity * price
        print(symbol.ljust(10) + str(quantity).ljust(8) + ("$" + str(price)).ljust(12) + "$" + str(value))

    print("-" * 50)
    print("TOTAL INVESTMENT VALUE: $" + str(total))
    print("=" * 50)


def save_to_file(portfolio, total):
    """Optionally save the result as a .txt or .csv file."""
    choice = ""
    while choice not in ["txt", "csv", "no"]:
        choice = input("\nSave results? Type 'txt', 'csv' or 'no': ").strip().lower()
        if choice not in ["txt", "csv", "no"]:
            print("Please type exactly 'txt', 'csv' or 'no'.")

    if choice == "no":
        print("Results were not saved.")
        return

    if choice == "txt":
        filename = "portfolio.txt"
        # 'w' means write mode - it creates the file or overwrites it.
        file = open(filename, "w")
        file.write("MY STOCK PORTFOLIO\n")
        file.write("------------------\n")
        for symbol in portfolio:
            value = portfolio[symbol] * STOCK_PRICES[symbol]
            file.write(symbol + " - " + str(portfolio[symbol]) + " shares @ $"
                       + str(STOCK_PRICES[symbol]) + " = $" + str(value) + "\n")
        file.write("------------------\n")
        file.write("Total Investment: $" + str(total) + "\n")
        file.close()
    else:
        filename = "portfolio.csv"
        file = open(filename, "w")
        file.write("Stock,Quantity,Price,Value\n")
        for symbol in portfolio:
            value = portfolio[symbol] * STOCK_PRICES[symbol]
            file.write(symbol + "," + str(portfolio[symbol]) + ","
                       + str(STOCK_PRICES[symbol]) + "," + str(value) + "\n")
        file.write("TOTAL,,," + str(total) + "\n")
        file.close()

    print("Saved successfully as '" + filename + "' in this folder.")


# ---------------------------------------------------------------
# 3. MAIN PROGRAM
# ---------------------------------------------------------------

def main():
    print("=" * 50)
    print("        STOCK PORTFOLIO TRACKER")
    print("=" * 50)
    print("Enter the stocks you own and this tool will")
    print("calculate your total investment value.")

    show_available_stocks()

    portfolio = build_portfolio()

    # An empty dictionary is treated as False in an if statement.
    if not portfolio:
        print("\nYou did not enter any stocks. Nothing to calculate. Goodbye!")
        return

    total = calculate_total(portfolio)
    display_portfolio(portfolio, total)
    save_to_file(portfolio, total)

    print("\nThank you for using the Stock Portfolio Tracker!")


if __name__ == "__main__":
    main()
