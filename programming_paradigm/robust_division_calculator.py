def safe_divide(numerator, denominator):
    try:
        numerator = float(numerator)
        denominator =float(denominator)
        result = numerator / denominator
        return f"The result of {numerator} / {denominator} is {result:.2f}"
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed"
    except ValueError:
        return "Error: Non-numeric input. Input a numrical value"