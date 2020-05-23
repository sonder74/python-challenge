import os
import csv

vote = 0
vote_list = []
khan_list = []
correy_list = []
li_list = []
otooley_list = []

def election_analyzer(election_data):
    vote = str(election_data[0])
    vote_list.append(vote)

    if election_data[2] == "Khan":
        khan_list.append(vote)

    else:

        if election_data[2] == "Correy":
            correy_list.append(vote)

        else:

            if election_data[2] == "Li":
                li_list.append(vote)

            else:

                if election_data[2] == "O'Tooley":
                    otooley_list.append(vote)

csvpath = os.path.join("election_data.csv")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    
    header = next(csvreader)

    for row in csvreader:
        election_analyzer(row)

vote_totals = [len(khan_list), len(correy_list), len(li_list), len(otooley_list)]

if max(vote_totals) == len(otooley_list):
    winner = "O'Tooley"

else:

    if max(vote_totals) == len(li_list):
        winner = "Li"

    else:

        if max(vote_totals) == len(correy_list):
            winner = "Correy"

        else:

            if max(vote_totals) == len(khan_list):
                winner = "Khan"

print("Election Results")
print("-----------------------")
print("Total Votes: " + str(len(vote_list)))
print("-----------------------")
print(f"Khan: {len(khan_list) / len(vote_list) * 100:.3f}% ({len(khan_list)})")
print(f"Correy: {len(correy_list) / len(vote_list) * 100:.3f}% ({len(correy_list)})")
print(f"Li: {len(li_list) / len(vote_list) * 100:.3f}% ({len(li_list)})")
print(f"O'Tooley: {len(otooley_list) / len(vote_list) * 100:.3f}% ({len(otooley_list)})")
print("-----------------------")
print("Winner: " + winner)
print("-----------------------")

file = open("main.py.txt", "w")
file.write("Election Results")
file.write("\n")
file.write("-----------------------")
file.write("\n")
file.write("Total Votes: " + str(len(vote_list)))
file.write("\n")
file.write("-----------------------")
file.write("\n")
file.write(f"Khan: {len(khan_list) / len(vote_list) * 100:.3f}% ({len(khan_list)})")
file.write("\n")
file.write(f"Correy: {len(correy_list) / len(vote_list) * 100:.3f}% ({len(correy_list)})")
file.write("\n")
file.write(f"Li: {len(li_list) / len(vote_list) * 100:.3f}% ({len(li_list)})")
file.write("\n")
file.write(f"O'Tooley: {len(otooley_list) / len(vote_list) * 100:.3f}% ({len(otooley_list)})")
file.write("\n")
file.write("-----------------------")
file.write("\n")
file.write("Winner: " + winner)
file.write("\n")
file.write("-----------------------")