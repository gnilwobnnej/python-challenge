#written by jennifer bowling

#importing things
import csv
import os

# location for input and output
f_load = os.path.join("Resources", "budget_data.csv")
f_out = os.path.join("analysis", "budget_analysis.txt")

#set values
t_months = 0
m_change = []
nc_list = []
increase = ["", 0]
decrease = ["", 99999]
total_net = 0

#read the csv
with open(f_load) as financial_data:
    reader = csv.reader(financial_data)

    header = next(reader)

    # take out the first row
    first_row = next(reader)
    t_months += 1
    total_net += int(first_row[1])
    prev_net = int(first_row[1])

    for row in reader:

        t_months += 1
        total_net += int(row[1])

        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        nc_list += [net_change]
        m_change += [row[0]]

        # calculate the increase
        if net_change > increase[1]:
            increase[0] = row[0]
            increase[1] = net_change

        # calculate the decrease
        if net_change < decrease[1]:
            decrease[0] = row[0]
            decrease[1] = net_change


net_monthly_avg = sum(nc_list) / len(nc_list)

#\n new line like java
output = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {t_months}\n"
    f"Total: ${total_net}\n"
    f"Average Change: ${net_monthly_avg:.2f}\n"
    f"Greatest Increase in Profits: {increase[0]} (${increase[1]})\n"
    f"Greatest Decrease in Profits: {decrease[0]} (${decrease[1]})\n")

#print the output 
print(output)

#save the output
with open(f_out, "w") as txt_file:
    txt_file.write(output)