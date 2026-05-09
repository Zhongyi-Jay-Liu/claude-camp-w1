def parse_tip(raw: str) -> float:
    """Accept '18', '18%', or '18 %' — always return a plain float."""
    return float(raw.strip().rstrip("%").strip())
def get_float(prompt: str, parser=float) -> float:
    """Prompt until the user enters a valid non-negative number."""
    while True:
        try:
            value = parser(input(prompt))
            if value < 0: print("  ⚠  Please enter a non-negative number.")
            else: return value
        except ValueError:
            print("  ⚠  Invalid input — please enter a number (e.g. 18 or 18%).")
def calculate_catering_bill(bill: float, tip_pct: float) -> dict:
    """Return itemised catering costs given a bill amount and tip percentage."""
    tip_amount = round(bill * tip_pct / 100, 2)
    return {"subtotal": bill, "tip_pct": tip_pct, "tip_amount": tip_amount, "total": round(bill + tip_amount, 2)}
def main():
    """Collect user input and display an itemised catering bill."""
    bill    = get_float("Enter catering bill amount ($): ")
    tip_pct = get_float("Enter tip percentage (e.g. 18 or 18%): ", parser=parse_tip)
    costs   = calculate_catering_bill(bill, tip_pct)
    print("\n--- Catering Cost Breakdown ---")
    print(f"  Subtotal : ${costs['subtotal']:.2f}")
    print(f"  Tip ({costs['tip_pct']}%) : ${costs['tip_amount']:.2f}")
    print(f"  {'─' * 22}")
    print(f"  Total    : ${costs['total']:.2f}")
if __name__ == "__main__":
    main()