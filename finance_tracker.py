import json, os
from datetime import datetime
 
 
# ── Base Transaction class ─────────────────────────────────────
class Transaction:
    def __init__(self, description, amount, category):
        self.description = description
        self._amount     = amount         # encapsulated
        self.category    = category
        self.date        = datetime.now().strftime("%Y-%m-%d")
 
    @property
    def amount(self):
        return self._amount
 
    @amount.setter
    def amount(self, value):
        if value <= 0: raise ValueError("Amount must be positive.")
        self._amount = value
 
    def to_dict(self):
        return {
            "type":        self.__class__.__name__,
            "description": self.description,
            "amount":      self._amount,
            "category":    self.category,
            "date":        self.date,
        }
 
    def __str__(self):
        return f"{self.date} | {self.category:<15} | {self.description:<25}"
 
 
# ── Income and Expense subclasses ─────────────────────────────
class Income(Transaction):
    def __init__(self, description, amount, category="Income"):
        super().__init__(description, amount, category)
 
    def __str__(self):
        return super().__str__() + f" | +NGN {self._amount:>12,.2f}"
 
 
class Expense(Transaction):
    def __init__(self, description, amount, category="Expense"):
        super().__init__(description, amount, category)
 
    def __str__(self):
        return super().__str__() + f" | -NGN {self._amount:>12,.2f}"
 
 
# ── Finance Tracker (the main manager class) ──────────────────
class FinanceTracker:
    FILE = "finances.json"
 
    def __init__(self):
        self.transactions = []
        self._load()
 
    def add(self, transaction):
        self.transactions.append(transaction)
        self._save()
        print(f"  Saved: {transaction}")
 
    @property
    def total_income(self):
        return sum(t.amount for t in self.transactions if isinstance(t, Income))
 
    @property
    def total_expenses(self):
        return sum(t.amount for t in self.transactions if isinstance(t, Expense))
 
    @property
    def balance(self):
        return self.total_income - self.total_expenses
 
    def summary(self):
        print(f"\n  {'=' * 50}")
        print(f"  FINANCE SUMMARY")
        print(f"  {'=' * 50}")
        print(f"  Total Income:   NGN {self.total_income:>12,.2f}")
        print(f"  Total Expenses: NGN {self.total_expenses:>12,.2f}")
        print(f"  {'-' * 50}")
        bal_str = f"NGN {abs(self.balance):>12,.2f}"
        sign    = "+" if self.balance >= 0 else "-"
        print(f"  Net Balance:    {sign}{bal_str}")
        print(f"  {'=' * 50}\n")
 
    def by_category(self):
        categories = {}
        for t in self.transactions:
            categories.setdefault(t.category, 0)
            if isinstance(t, Expense):
                categories[t.category] += t.amount
        print("\n  Spending by Category:")
        for cat, total in sorted(categories.items(), key=lambda x: x[1], reverse=True):
            print(f"    {cat:<20} NGN {total:>12,.2f}")
 
    def recent(self, n=5):
        last_n = self.transactions[-n:]
        print(f"\n  Last {n} transactions:")
        for t in reversed(last_n):
            print(f"  {t}")
 
    def _save(self):
        data = [t.to_dict() for t in self.transactions]
        with open(self.FILE, "w") as f:
            json.dump(data, f, indent=2)
 
    def _load(self):
        if not os.path.exists(self.FILE): return
        with open(self.FILE) as f:
            data = json.load(f)
        for item in data:
            cls = Income if item["type"] == "Income" else Expense
            t   = cls(item["description"], item["amount"], item["category"])
            t.date = item["date"]
            self.transactions.append(t)
 
 
# ── Main menu ─────────────────────────────────────────────────
def main():
    tracker = FinanceTracker()
    while True:
        print("\n  1) Add Income    2) Add Expense")
        print("  3) Summary       4) By Category")
        print("  5) Recent        0) Quit")
        choice = input("\n  Choice: ").strip()
        try:
            if choice == "1":
                desc  = input("  Description: ")
                amt   = float(input("  Amount: NGN "))
                cat   = input("  Category (default: Income): ") or "Income"
                tracker.add(Income(desc, amt, cat))
            elif choice == "2":
                desc  = input("  Description: ")
                amt   = float(input("  Amount: NGN "))
                cat   = input("  Category (Food/Transport/Bills/etc): ")
                tracker.add(Expense(desc, amt, cat))
            elif choice == "3": tracker.summary()
            elif choice == "4": tracker.by_category()
            elif choice == "5": tracker.recent()
            elif choice == "0": print("  Goodbye!"); break
        except ValueError as e:
            print(f"  Error: {e}")
 
if __name__ == "__main__":
    main()



# •	Add a search_by_description(keyword) method — case-insensitive, returns matching transactions
# •	Add a filter_by_date_range(start_date, end_date) method — filter by "YYYY-MM-DD" strings
# •	Add a monthly_summary() method — group and total transactions by month
# •	Add a BudgetCategory class — set a spending limit per category and warn when exceeded

# Challenge: Add CSV export export all transactions to a .csv file with headers Date, Type, Category, Description, Amount.


# Files
# # Write
# with open("file.txt", "w") as f: f.write("text\n")
# # Append
# with open("file.txt", "a") as f: f.write("more\n")
# # Read all
# with open("file.txt", "r") as f: content = f.read()
# # Read lines
# with open("file.txt", "r") as f: lines = f.readlines()
# with open("file.txt", "r") as f:
#     for line in f: print(line.strip())

# JSON
# import json
# json.dumps(obj)          # obj -> JSON string
# json.loads(text)         # JSON string -> obj
# json.dump(obj, f)        # obj -> write to file
# json.load(f)             # read file -> obj
# json.dumps(obj, indent=4)  # pretty-printed




# Error Handling
# try:
#     risky()
# except ValueError as e:
#     print(e)
# except (TypeError, KeyError):
#     handle_both()
# else:
#     success()    # only if no exception
# finally:
#     cleanup()    # always


# Class Template
# class MyClass(ParentClass):
#     def __init__(self, x, y):
#         super().__init__(x)
#         self.y = y
 
#     @property
#     def y(self): return self._y
 
#     @y.setter
#     def y(self, val):
#         if val < 0: raise ValueError("...")
#         self._y = val
 
#     def to_dict(self):
#         return {"x": self.x, "y": self._y}
 
#     @classmethod
#     def from_dict(cls, d): return cls(d["x"], d["y"])
 
#     def __str__(self): return f"MyClass({self.y})"






# Functional Tools
# sorted(L, key=lambda x: x["field"], reverse=True)
# list(map(lambda x: x*2, numbers))
# list(filter(lambda x: x>0, numbers))
 
# # Comprehensions
# [expr for item in L if cond]
# {k: v for k, v in d.items() if cond}
# {expr for item in L}





# Key Imports
# import json, os, math, random
# from datetime import datetime, date, timedelta
# from math import sqrt, pi, floor, ceil

