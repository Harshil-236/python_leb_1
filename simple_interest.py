def calculate_simple_interest(principal, time, rate):
    simple_interest = (principal * time * rate) / 100
    return simple_interest

# Input values
principal = 1000
time = 2
rate = 5

# Calculate simple interest
result = calculate_simple_interest(principal, time, rate)
print("Simple Interest:", result)
