
# Name: Muiz Ajiboye
# Student ID: 18436684
# Date: 20/01/2024

# Create a list to store the number of customers each day
customer_count = []

# Use a for loop to ask the user to input the number of customers over a 7-day period
for day in range(1, 8):  # Loop for 7 days
    try:
        # Get user input for the number of customers and convert it to an integer
        customers = int(input(f"Enter the number of customers for day {day}: "))

        # Append the number of customers to the list
        customer_count.append(customers)
    except ValueError:
        # Handle the case where the user enters a non-integer value
        print("Invalid input. Please enter a valid integer.")

# Determine the maximum, minimum, and average number of customers
max_customers = max(customer_count)
min_customers = min(customer_count)
average_customers = sum(customer_count) / len(customer_count) if len(customer_count) > 0 else 0

# Display the list of customer counts
print("\nCustomer counts for each day:", customer_count)

# Print the maximum, minimum, and average number of customers
print("Maximum number of customers:", max_customers)
print("Minimum number of customers:", min_customers)
print("Average number of customers:", round(average_customers, 2))
