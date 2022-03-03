# 1. Retrieve data
# 1.1 Load the file, assign input and output file to variable
import csv
import os

file_to_load=os.path.join("Resources","election_results.csv")

file_to_save=os.path.join("analysis","election_analysis.txt")

# 1.2 Initialize needed variables
# 1.2.1 Total votes is needed as an integer
total_votes=0
# 1.2.2 Candidate Options is needed as a list
candidate_options = []
# 1.2.3 The votes per candidate is needed as a dictionary.
candidate_votes = {}
# 1.2.4 Add Winning Candidate variables, name is a string, the others are set to zero.
winning_candidate = ""
winning_count = 0
winning_percentage = 0


# 1.3 Open election results, this makes the file as an object
with open(file_to_load) as election_data:

    # 1.3.1 The file object is now converted into a list of dictionaries with reader function.
    file_reader = csv.reader(election_data)

    # 1.3.2 The header row needs to be skipped.
    headers = next(file_reader)

    #2. We will iterate through each row to get the required information fron file
    for row in file_reader:
        # 2.1 We are getting a counter for total votes.
        total_votes += 1

        # 2.2 Get a list of candidate names
        # 2.2.1 Grab the candidate name for each row
        candidate_name = row[2]

        # 2.2.2 Add all the names to candidate list, evaluate if candidate is already part of list.
        if candidate_name not in candidate_options:
            # 2.2.2.1 Add it to the list of candidates.
            candidate_options.append(candidate_name)
           # 2.3 Get the number of votes per candidate.
           # 2.3.1 Set all the candidate votes to zero.
            candidate_votes[candidate_name] = 0
        # 2.3.2 Add a vote to that candidate's count. Output is a dictionary.
        candidate_votes[candidate_name] += 1
    
    # 3.Evaluate data
    # 3.1 Determine the percentage of votes for each candidate by looping through the counts.
    # 3.1.1 Iterate through the candidate list.
    for candidate_name in candidate_votes:
        # 3.1.2 Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        # 3.1.3 Calculate the percentage of votes. Turn votes and total votes into a float point decimal.
        vote_percentage = float(votes) / float(total_votes) * 100
        # 3.1.4 Print the candidate name and percentage of votes.
        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # 3.2 Determine winning candidate
        # 3.2.1 Evaluate if the votes for each cancidate is greater than the ones evaluated before.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # 3.2.2 If true then set winning_count = votes and winning_percent =
            # vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
            # 3.2.3 Set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name

    #4. Print the winning candidate results
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)