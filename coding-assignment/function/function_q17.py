#Write a function to calculate simple interest.
def simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

print(simple_interest(1000, 5, 2))  # Output: 100.0
