##You will be given a set of poll data called `election_data.csv`. The dataset is composed of three columns: "Voter ID", "County", and "Candidate". 
#Your task is to create a Python script that analyzes the votes and calculates each of the following values:

#* The total number of votes cast

#* A complete list of candidates who received votes

#* The percentage of votes each candidate won

#* The total number of votes each candidate won

#* The winner of the election based on popular vote

import os
import csv

csvpath =os.path.join("/Users/irena/Desktop/pythonchallenge/PyPoll/Resources/election_data.csv")
csvpath_output = ("/Users/irena/Desktop/pythonchallenge/PyPoll/Resources/election_data.txt")

# Setting up variables

votes = 0
total_candidates = 0
winner_votes = 0
greatest_votes = ["",0]
candidate_options = []
candidate_votes = {}

#Read through the csv and collect our data

with open(csvpath) as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        votes = votes + 1
        total_candidates = row["Candidate"]

        if row ["Candidate"] not in candidate_options:
            candidate_options.append(row["Candidate"])
            candidate_votes[row["Candidate"]] = 1

        else:
            candidate_votes[row["Candidate"]] = candidate_votes[row["Candidate"]] + 1
    
    if (votes > winner_votes):
        greatest_votes[1] = candidate_votes
        greatest_votes[0] = row["Candidate"]
    
    print("Election Results")
    print("----------------------------")
    print("Total Votes" + str(votes))
    print("----------------------------")

    for candidate in candidate_votes:
        print(candidate + " " + str(round(((candidate_votes[candidate]/votes)*100))) + "%" + "(" + str(candidate_votes[candidate]) + ")")
        candidate_results = (candidate + " " + str(round(((candidate_votes[candidate]/votes)*100)))) + "%" + "(" + str(candidate_votes[candidate]) + ")"

candidate_votes

winner = sorted(candidate_votes.items(),)

print("-------------------------")
print("Winner: " + str(winner[1]))
print("-------------------------")

#create txt file

with open(csvpath_output, "w") as txt_file:
    
    txt_file.write("Election Results")
    txt_file.write("\n")
    txt_file.write("-------------------------")
    txt_file.write("\n")
    txt_file.write(candidate + " " + str(round(((candidate_votes[candidate]/votes)*100))) + "%" + " (" + str(candidate_votes[candidate]) + ")")
    txt_file.write(str(winner))
    txt_file.write("\n")
    txt_file.write("-------------------------")
    txt_file.write("\n")
    txt_file.write("Winner: " + str(winner[1]))
    txt_file.write("\n")
    txt_file.write("Total Votes " + str(votes))