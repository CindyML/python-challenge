import os
import csv
import subprocess

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
    winner = Candidate1
    #print("Winner:", (Candidate1))
elif Largest_value == Candidate2_percent:
    winner = Candidate2
    #print("Winner:", (Candidate2))
elif Largest_value == Candidate3_percent:
    winner = Candidate3
    #print("Winner:", (Candidate3))
else: 0
print("Winner", winner)
print()
print("---------------------------")

#file_name = "PyPoll_Results(code).txt"
#open(file_name, "w")

#input_file = (C:/Users/cynth/Python-challenge/PyPoll/main.py)
input_file_path = ("C:", "Users", "cynth", "Python-challenge", "PyPoll", "main.py")
#output_file = (C:/Users/cynth/Python-challenge/PyPoll/PyPoll_Results(code).txt)
output_file_path = ("C:", "Users", "cynth", "Python-challenge", "PyPoll", "PyPoll_Results(code).txt")

input_file_path = '/'.join(input_file_path)
output_file_path = '/'.join(output_file_path)


#with open(input_file_path, 'r') as input_file:
    #code = input_file.read()

#with open(output_file_path, 'w') as output_file:
    #output_file.write(code)

#print_code_to_file(input_file, output_file)

with open(output_file_path, 'w') as output_file:
    output = (f"Election Results\n"
              f"\n"
              f"---------------------------\n"
              f"\n"
              f"Total Votes: {row_count}\n"
              f"\n"
              f"---------------------------\n" 
              f"\n"
              f"Charles Caspter Stockham: {formatted_percentage1}, {str(row_count1)}\n"
              f"\n"
              f"Diana DeGette: {formatted_percentage2}, {str(row_count2)}\n"
              f"\n"
              f"Raymon Anthony Doane: {formatted_percentage3}, {str(row_count3)}\n"
              f"\n"
              f"---------------------------\n"
              f"\n"
              f"Winner: {winner}\n"
              f"\n"
              f"---------------------------")
              
    
    output_file.write(output)
    #subprocess.run(["python", input_file_path], stdout=output_file, text=True)  
    # Redirect output to file
#import sys
#sys.stderr = output_file

#print(f"Script results saved to: {output_file_path}", flush=True)