import os
import csv

budget_data = os.path.join("..", "PyBank", "Resources", "budget_data.csv")

header_rows = [
            "Financial Analysis",
            "",
            "---------------------------",
            "",
        ]

for header_row in header_rows:
    print(header_row)

average_difference = (budget_data, 1)
differences = []
                            
row_count = 0
total_amount = 0
previous_value = None   

with open(budget_data) as csvfile:
    csv_reader = csv.reader(csvfile)
    next(csv_reader)
    for row in csv_reader:
        row_count += 1
        try:
            value = float(row[1])
            total_amount += value
            current_value = float(row[1])

            if previous_value is not None:
                difference = current_value - previous_value
                differences.append(difference)
            previous_value = current_value
            max_difference = max(differences)
            min_difference = min(differences)        

        except ValueError:
            pass
if differences:
    average_difference = round((sum(differences) / len(differences)), ndigits=2)
else:
    0

rounded_int = round(total_amount)
rounded_int2 = round(max_difference)
rounded_int3 = round(min_difference)
        
print("Total Months:", row_count)
print()
print("Total:", "$" + str(rounded_int))
print()
print("Average Change:", "$" + str(average_difference))
print()
print("Greatest Increase in Profits:", row[0], "($" + str(rounded_int2) + ")")
print()
print("Greatest Decrease in Profits:", row[0], "($" + str(rounded_int3) + ")")
print()

#the below doesn't export content to the text file, but creates the text file
#file_name = "PyBank_Results(code)2.txt"
#with open(file_name, "w") as file:
    #message = "Financial Analysisvn\ n\ --------------------------- n\ n\ Total Months: {row_count}"
    #print(message)

#input_file = (C:/Users/cynth/Python-challenge/PyPoll/main.py)
input_file_path = ("C:", "Users", "cynth", "Python-challenge", "PyBank", "main.py")
#output_file = (C:/Users/cynth/Python-challenge/PyPoll/PyPoll_Results(code).txt)
output_file_path = ("C:", "Users", "cynth", "Python-challenge", "PyBank", "PyBank_Results(code)2.txt")

input_file_path = '/'.join(input_file_path)
output_file_path = '/'.join(output_file_path)

with open(output_file_path, 'w') as output_file:
    output = (f"Financial Analysis\n"
              f"\n"
              f"---------------------------\n"
              f"\n"
              f"Total Months: {row_count}\n"
              f"\n"
              f"Total: ${rounded_int}\n"
              f"\n"
              f"Average Change: ${average_difference}\n"
              f"\n"
              f"Greatest Increase in Profits: row[0], ${rounded_int2}\n"
              f"\n"
              f"Greatest Decrease in Profits: row[0], ${rounded_int3}\n"
              f"\n")
    
    output_file.write(output)

