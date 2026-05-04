# ── File: calculator.py ──
def add(a, b): return a + b
def multiply(a, b): return a * b
 
if __name__ == "__main__":
    # This block ONLY runs when you type: python calculator.py
    # It does NOT run when another file does: import calculator
    print("Testing calculator module...")
    print(add(3, 4))        # 7
    print(multiply(5, 6))   # 30
    print("All tests passed!")
