#Write a function to check if a number is positive, negative, or zero.
def check_number(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    return "Zero"

print(check_number(5))   # Output: Positive
print(check_number(-3))  # Output: Negative
print(check_number(0))   # Output: Zero
