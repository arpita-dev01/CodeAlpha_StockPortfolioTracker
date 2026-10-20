# CodeAlpha_StockPortfolioTracker

**CodeAlpha Python Programming Internship — Task 2: Stock Portfolio Tracker**

A console tool that calculates the total value of a stock portfolio using
manually defined (hardcoded) stock prices. No API and no internet connection
are required.

---

## Task Requirements (from CodeAlpha)

| Requirement | Status |
|---|---|
| User inputs stock names and quantity | Done |
| Hardcoded dictionary of stock prices | Done |
| Display total investment value | Done |
| Optionally save result to .txt or .csv | Done |
| Key concepts: dictionary, input/output, arithmetic, file handling | Done |

---

## How to Run

```bash
python stock_tracker.py
```

On macOS/Linux use `python3 stock_tracker.py`.

---

## How to Use

1. The program lists the stocks it knows and their prices.
2. Type a stock symbol (e.g. `AAPL`), then the number of shares you own.
3. Repeat for as many stocks as you like.
4. Type `done` when finished.
5. A table of holdings and the total investment value is shown.
6. Choose to save the result as `portfolio.txt`, `portfolio.csv`, or not at all.

---

## Features

- Prices stored in a Python **dictionary** (`STOCK_PRICES`)
- Rejects unknown symbols, empty input, non-numeric quantities and zero quantity
- Entering the same stock twice **adds** to the existing quantity instead of
  overwriting it
- Formatted output table
- File handling: exports to plain text or CSV (CSV opens directly in Excel)

---

## Sample Output

```
==================================================
             YOUR STOCK PORTFOLIO
==================================================
STOCK     QTY     PRICE       VALUE
--------------------------------------------------
AAPL      15      $180        $2700
TSLA      5       $250        $1250
--------------------------------------------------
TOTAL INVESTMENT VALUE: $3950
==================================================
```

---

## Project Structure

```
CodeAlpha_StockPortfolioTracker/
├── stock_tracker.py
├── README.md
└── .gitignore
```

---

## Author

Submitted as part of the CodeAlpha Python Programming Internship.
