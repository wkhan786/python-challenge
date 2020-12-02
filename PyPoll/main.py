#You will be give a set of poll data called election_data.csv. The dataset is composed of three columns: Voter ID, County, and Candidate. Your task is to create a Python script that analyzes the votes and calculates each of the following:
#The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote.

import os
import csv

# List to capture candidate names
candidates = []

# List to capture the number of votes each candidate receives
number_votes = []

# List to capture the percentage of total votes each candidate receives 
percentage_votes = []

# A counter for the total number of votes 
total_votes = 0

with open("Resources/election_data.csv", "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader)

    for row in csvreader:
        # Add to vote-counter 
        total_votes += 1 

        if row[2] not in candidates:
            candidates.append(row[2])
            index = candidates.index(row[2])
            number_votes.append(1)
        else:
            index = candidates.index(row[2])
            number_votes[index] += 1
    
    # Add to percentage_votes list 
    for votes in number_votes:
        percentage = (votes/total_votes) * 100
        percentage = str(round(percentage, 3)) + "%"
        percentage_votes.append(percentage)
    
    # Find the winning candidate
    winner = max(number_votes)
    index = number_votes.index(winner)
    winning_candidate = candidates[index]

#Displaying rersults
OutputAnalysis=(
    f"Election Results\n"
    f"Total Votes: {total_votes}\n"
    )

for i in range(len(candidates)):
    OutputAnalysis += (
        f"{candidates[i]}: {(percentage_votes[i])} ({(number_votes[i])})\n"
        )
OutputAnalysis += f"Winner: {winning_candidate}\n"
print(OutputAnalysis)

# Exporting to .txt file
with open("Analysis/output.txt", "w") as output:
    output.write(OutputAnalysis)

