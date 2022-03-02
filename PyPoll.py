# 1. Retrieve data
# 1.1 Load the file, assign file to variable
import csv
import os

file_to_load=os.path.join("Resources","election_results.csv")

#1.2 Create a file for results

file_to_save=os.path.join("analysis","election_analysis.txt")

# 1.2 Open election results and read file
with open(file_to_load) as election_data:

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Print each row in the CSV file.
    for row in file_reader:
        print(row)
        
# 1.3.1 Open the file
   
    # Write three counties to the file.
    
# 2. Get total number of votes casted

# 3. Get list of candidates

# 4. Get total votes per candidate

# 5. Calculate vote percentages per candidates

# 6. Identify candidate with most votes, aka winner