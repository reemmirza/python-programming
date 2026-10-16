
def add(a: float, b: float) -> float:
    """Return the sum of a and b."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Return a minus b."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Return a times b."""
    return a * b


def divide(a: float, b: float) -> float:
    """Return a divided by b."""
    if b == 0:
        raise ValueError("Divisor cannot be zero.")
    return a / b

def main():
    print("Hello World")

if __name__ == "__main__":
    main()