#written by jennifer bowling

#importing what I need
import csv
import os

# file to read from and where to save
f_load = os.path.join("Resources", "election_data.csv")
f_output = os.path.join("analysis", "election_analysis.txt")


tVotes = 0
c_options = []
c_votes = {}
wCan = ""
wCount = 0


with open(f_load) as election_data:
    reader = csv.reader(election_data)

    header = next(reader)

    for row in reader:

        print(". ", end=""),
        tVotes = tVotes + 1
        cName = row[2]
        if cName not in c_options:
            c_options.append(cName)
            c_votes[cName] = 0
        c_votes[cName] = c_votes[cName] + 1


with open(f_output, "w") as txt_file:

    election_results = (
        f"\n\nElection Results\n\n"
        f"-------------------------\n\n"
        f"Total Votes: {tVotes}\n\n"
        f"-------------------------\n\n")
    print(election_results, end="")


    txt_file.write(election_results)
    for candidate in c_votes:
        votes = c_votes.get(candidate)
        vote_percentage = float(votes) / float(tVotes) * 100
        if (votes > wCount):
            wCount = votes
            wCan = candidate

 
        voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n\n"
        print(voter_output, end="")


        txt_file.write(voter_output)


    wCan_summary = (
        f"-------------------------\n\n"
        f"Winner: {wCan}\n\n"
        f"-------------------------\n\n")
    print(wCan_summary)

    # save the file
    txt_file.write(wCan_summary)