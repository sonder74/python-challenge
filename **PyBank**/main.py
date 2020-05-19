import os
import csv

month = 0
monthly_cash = 0
month_list = []
monthly_cash_list = []

def financial_analyzer(budget_data):
    month = str(budget_data[0])
    month_list.append(month)
    monthly_cash = int(budget_data[1])
    monthly_cash_list.append(monthly_cash)

csvpath = os.path.join("budget_data.csv")

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    
    header = next(csvreader)

    for row in csvreader:
        financial_analyzer(row)
        change_list = [monthly_cash_list[i + 1] - monthly_cash_list[i] for i in range(len(monthly_cash_list) - 1)]

    average_change = round(sum(change_list) / len(change_list),2)
    max_pos = change_list.index(max(change_list))
    min_pos = change_list.index(min(change_list))

print("Financial Analysis")
print("---------------------------")
print("Total Months: " + str(len(month_list)))
print("Total: $" + str(sum(monthly_cash_list)))
print("Average Change: $" + str(average_change))
print("Greatest Increase in Profits: " + str(month_list[max_pos + 1]) + " ($" + str(max(change_list)) + ")")
print("Greatest Decrease in Profits: " + str(month_list[min_pos +1]) + " ($" + str(min(change_list)) + ")")

file = open("main.py.txt", "w")
file.write("Financial Analysis")
file.write("\n")
file.write("---------------------------")
file.write("\n")
file.write("Total Months: " + str(len(month_list)))
file.write("\n")
file.write("Total: $" + str(sum(monthly_cash_list)))
file.write("\n")
file.write("Average Change: $" + str(average_change))
file.write("\n")
file.write("Greatest Increase in Profits: " + str(month_list[max_pos + 1]) + " ($" + str(max(change_list)) + ")")
file.write("\n")
file.write("Greatest Decrease in Profits: " + str(month_list[min_pos +1]) + " ($" + str(min(change_list)) + ")")