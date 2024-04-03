import os
import csv

election_data = os.path.join("..", "PyPoll", "Resources", "election_data.csv")

header_rows = [
            "Election Results",
            "",
            "---------------------------",
            "",
        ]

for header_row in header_rows:
    print(header_row)

row_count = 0
Candidate1 = "Charles Casper Stockham"
Candidate2 = "Diana DeGette"
Candidate3 = "Raymon Anthony Doane"
row_count1 = 0
row_count2 = 0
row_count3 = 0


with open(election_data) as csvfile:
    csv_reader = csv.reader(csvfile)
    next(csv_reader)
    for row in csv_reader:
        row_count += 1
        if row[2] == Candidate1:
            row_count1 += 1
        Candidate1_percent = (row_count1 / row_count) * 100
        formatted_percentage1 = f"{Candidate1_percent: .3f}%"
        if row[2] == Candidate2:
            row_count2 += 1
        Candidate2_percent = (row_count2 / row_count) * 100
        formatted_percentage2 = f"{Candidate2_percent: .3f}%"
        if row[2] == Candidate3:
            row_count3 += 1
        Candidate3_percent = (row_count3 / row_count) * 100
        formatted_percentage3 = f"{Candidate3_percent: .3f}%"
   

print("Total Votes:", row_count)
print()
print("---------------------------")
print()
print("Charles Caspter Stockham:", (formatted_percentage1), "(" + str(row_count1) + ")")
print()
print("Diana DeGette:", (formatted_percentage2), "(" + str(row_count2) + ")")
print()
print("Raymon Anthony Doane", (formatted_percentage3), "(" + str(row_count3) + ")")
print()
print("---------------------------")
print()
values = [Candidate1_percent, Candidate2_percent, Candidate3_percent]
Largest_value = max(values)
if Largest_value == Candidate1_percent:
    print("Winner:", (Candidate1))
elif Largest_value == Candidate2_percent:
    print("Winner:", (Candidate2))
elif Largest_value == Candidate3_percent:
    print("Winner:", (Candidate3))
else: 0
print()
print("---------------------------")

file_name = "PyPoll_Results(code).txt"
open(file_name, "w")

