# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0

# Define a dictionary to track candidates and their vote counts
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0.0

# Open the CSV file and process it
try:
    with open(file_to_load) as election_data:
        reader = csv.reader(election_data)

        # Skip the header row
        header = next(reader)

        # Loop through each row of the dataset and process it
        for row in reader:
            # Increment the total vote count
            total_votes += 1

            # Get the candidate's name from the row (assuming it's in the 3rd column)
            candidate_name = row[2]

            # Add the candidate to the dictionary or increment their vote count
            if candidate_name not in candidate_votes:
                candidate_votes[candidate_name] = 1
            else:
                candidate_votes[candidate_name] += 1
except FileNotFoundError:
    print(f"Error: The file {file_to_load} was not found.")
    exit()

# Open a text file to save the output
with open(file_to_output, "w") as txt_file:

    # Print the total vote count (to terminal)
    print(f"Total Votes: {total_votes}")
    txt_file.write(f"Total Votes: {total_votes}\n")

    # Loop through the candidates to determine vote percentages and identify the winner
    for candidate_name in candidate_votes:

        # Get the vote count and calculate the percentage
        vote_count = candidate_votes[candidate_name]
        vote_percent = (vote_count / total_votes) * 100
        vote_percent_rounded = round(vote_percent, 3)

        # Update the winning candidate if this one has more votes
        if vote_count > winning_count:
            winning_count = vote_count
            winning_candidate = candidate_name
            winning_percentage = vote_percent_rounded

        # Print and save each candidate's vote count and percentage
        candidate_result = f"{candidate_name}: {vote_percent_rounded}% ({vote_count})\n"
        print(candidate_result, end="")
        txt_file.write(candidate_result)

    # Generate and print the winning candidate summary
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n"
    )

    # Save the winning candidate summary to the text file
    txt_file.write(winning_candidate_summary)

print("Election analysis complete! Results have been saved to election_analysis.txt.")
