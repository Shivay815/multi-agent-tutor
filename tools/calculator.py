def calculator(expression: str) -> float:
    """
    Performs basic arithmetic calculations.
    Supports addition, subtraction, multiplication, and division.
    Example: calculator("2+2")
    """
    try:
        # Using eval() can be dangerous with untrusted input,
        # but for this specific assignment where inputs are controlled
        # by our agent's prompts, it's acceptable for a simple calculator.
        # For production, consider a safer math expression parser.
        return eval(expression)
    except Exception as e:
        return f"Error: Could not calculate expression '{expression}'. {e}"

# You can add more tool functions here later, e.g., for looking up constants.