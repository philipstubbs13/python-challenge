# Dependencies
import pandas as pd
import os

# Create reference to the csv file
csv_file = "Resources/election_data.csv"

# Read in csv using pandas
election_data_df = pd.read_csv(csv_file)

# Print the first 5 lines of dataframe.
election_data_df.head()

# Calculate the total number of votes cast
num_votes = election_data_df["Voter ID"].count()

print(f"Total number of votes cast: {num_votes}")

# Get a complete list of candidates who received votes
list_candidates = election_data_df["Candidate"].unique()

list_candidates

# Calculate the total number of votes each candidate won
num_votes_list = []
for candidate in list_candidates:
    votes_for_candidate_df = election_data_df.loc[election_data_df["Candidate"] == candidate]
    num_votes_candidate = votes_for_candidate_df["Voter ID"].count()
    num_votes_list.append(num_votes_candidate)

print(num_votes_list)

# Calculate the percentage of votes each candidate won
percent_votes_list = []
for vote_count in num_votes_list:
    percent_votes_candidate = (vote_count / num_votes) * 100
    percent_votes_candidate = round(percent_votes_candidate, 2)
    percent_votes_list.append(percent_votes_candidate)

print(percent_votes_list)

# Calculate the winner of the election based on popular vote.

# Construct dictionary of lists to get election results.
election_results_dict = {
    "Candidates": list_candidates,
    "Number of Votes": num_votes_list,
    "Percentage of Votes (%)": percent_votes_list
}

# Create dataframe from dictionary of lists.
election_results_df = pd.DataFrame(election_results_dict)

# Sort results in descending order to determine winner.
election_results_descending_df = election_results_df.sort_values(
    "Number of Votes", ascending=False)

# Reset index of sorted results.
election_results_descending_df = election_results_descending_df.reset_index(
    drop=True)

# Store winner in variable.
winner = election_results_descending_df.iloc[0]['Candidates']
print(f"Winner: {winner}")

# Print results in descending order.
election_results_descending_df

# Print analysis

print("Election Results")
print("---------------------------------------------------------------")
print(f"Total votes: {num_votes}")
print("---------------------------------------------------------------")
print(election_results_descending_df.to_string(index=False))
print("---------------------------------------------------------------")
print(f"Winner: {winner}")
print("---------------------------------------------------------------")

# Export a text file with the results.
with open("election_results.txt", 'w') as file:

    file.write("Election Results\r\n")
    file.write(
        "---------------------------------------------------------------\r\n")
    file.write(f"Total votes: {num_votes}\r\n")
    file.write(
        "---------------------------------------------------------------\r\n")
    file.write(election_results_descending_df.to_string(index=False))
    file.write(
        "---------------------------------------------------------------\r\n")
    file.write(f"Winner: {winner}\r\n")
    file.write(
        "---------------------------------------------------------------\r\n")
