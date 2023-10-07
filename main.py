# Function to calculate the final amount for "Primer Broker"
def calculate_primer_broker(months, initial_amount):
    # Monthly subscription cost for Primer Broker
    monthly_cost_primer = 2.99
    # Calculate the total subscription cost for the given number of months
    total_cost_primer = monthly_cost_primer * months
    # Calculate the final amount after subscription costs
    final_amount_primer = initial_amount - total_cost_primer
    return final_amount_primer

# Function to calculate the final amount for "Prime + Broker"
def calculate_prime_plus_broker(months, initial_amount):
    # Monthly subscription cost for Prime + Broker
    monthly_cost_prime = 4.99
    # Annual interest rate for Prime + Broker
    annual_interest_prime = 0.026
    # Calculate the quarterly interest rate
    quarterly_interest_prime = annual_interest_prime / 4
    
    final_amount_prime = initial_amount
    
    # Calculate the final amount for each quarter
    for quarter in range(months // 3):
        # Deduct the quarterly subscription cost
        final_amount_prime -= (monthly_cost_prime * 3)
        # Add the quarterly interest
        final_amount_prime += (final_amount_prime * quarterly_interest_prime)
    
    # Handle remaining months if the total months are not a multiple of 3
    remaining_months = months % 3
    final_amount_prime -= (monthly_cost_prime * remaining_months)
    
    return final_amount_prime

# Function to find the threshold where "Prime + Broker" becomes more beneficial
def find_threshold(months):
    initial_amount = 100  # Start with an initial amount of €100
    increment = 1  # Increment the initial amount by €100 in each iteration
    threshold_found = False  # Flag to indicate if the threshold has been found
    
    # Keep iterating until "Prime + Broker" becomes more beneficial
    while not threshold_found:
        final_amount_primer = calculate_primer_broker(months, initial_amount)
        final_amount_prime = calculate_prime_plus_broker(months, initial_amount)
        
        if final_amount_prime > final_amount_primer:
            threshold_found = True  # Stop the loop
        else:
            initial_amount += increment  # Increment and try again
    
    return initial_amount

# Rest of the script remains unchanged


# Test calculations with an initial amount of €10,000 for 12 months
initial_amount = 10000
months = 12
final_amount_primer = calculate_primer_broker(months, initial_amount)
final_amount_prime = calculate_prime_plus_broker(months, initial_amount)

print(f"With €{initial_amount} for {months} months:")
print(f"Final amount with Primer Broker: €{final_amount_primer}")
print(f"Final amount with Prime + Broker: €{final_amount_prime}")

# Find the threshold for 12 months
threshold = find_threshold(12)
print(f"The threshold amount for 12 months is €{threshold}")