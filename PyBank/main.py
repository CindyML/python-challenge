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
file_name = "PyBank_Results(code)2.txt"
open(file_name, "w") 

