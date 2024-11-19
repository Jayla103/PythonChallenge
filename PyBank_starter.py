# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path



# Define variables to track the financial data
total_months = 0
total_net = 0
# Add more variables to track other necessary financial data
net_change_list = []
month_of_changes = []
greatest_increase = ["", 0]
greatest_decrease = ["", 99999999999999999999]

change_profit = {}

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)
 
    # Extract first row to avoid appending to net_change_list
    first_row = next(reader)
    total_months = total_months + 1
    total_net = total_net + int(first_row[1])
    prev_net = int(first_row[1])
    



    # Track the total and net change
    total_net = total_net

    # Process each row of data
    for row in reader:
    

        # Track the total
        total_months = total_months + 1
        total_net = total_net + int(row[1])

        # Track the net change
        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        net_change_list = net_change_list + [net_change]
        month_of_changes = month_of_changes + [row[1]]


        # Calculate the greatest increase in profits (month and amount)
        if net_change > greatest_increase[1]:
            greatest_increase[0] = row[0]  
            greatest_increase[1] = net_change

        # Calculate the greatest decrease in losses (month and amount)
        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change


# Calculate the average net change across the months
net_monthly_average = sum(net_change_list) / len(net_change_list)


# Generate the output summary
print(f"Total Months: {total_months}")

print(f"Total: ${total_net}")

print(f"Average Change: ${net_monthly_average}")

print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")

print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")


# Print the output

print(file_to_output)

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(file_to_output)
