def calculate_remainder(dividend, divisor):
    if divisor == 0:
        raise ValueError("Division by zero is not allowed.")
    remainder = dividend % divisor
    if remainder != 0 and ((dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0)):
        remainder -= divisor if dividend > 0 else -divisor
    return remainder
