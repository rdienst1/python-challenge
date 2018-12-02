#Instruction: Analyze the financial records of your company, contained in set of financial data called budget_data.csv

#The OS module in Python provides a way of using operating system dependent functionality.
import os
import csv
#Import csv working file: budget_data.csv
csvpath = os.path.join('C:\\Users\\Rob\\Documents\\03-Python\\Instructions\\PyBank\\Resources\\budget_data.csv')
newfile = os.path.join('C:\\Users\\Rob\\Documents\\03-Python\\Instructions\\PyBank\\Resources\\budget_final.txt')

#Financial Data
net_changes = []
total_net_profit = 0
greatest_increase = ["",0]
greatest_decrease = ["",99999999999999999]
month = []
month_total = 0
#Open and read the csv file
with open(csvpath, newline="") as budget_data:
   csv_reader = csv.reader(budget_data, delimiter=",")

# Read and take out the header row
   title = next(csv_reader)
   first_row = next(csv_reader)

   # Calculate total of months and profit
   month_total = month_total + 1
   total_net_profit = total_net_profit + int(first_row[1])
   previous = int(first_row[1])

   # For loop to gather financial data in csv
   for row in csv_reader:

       #Total months and profit
           month_total = month_total + 1
           total_net_profit = total_net_profit + int(row[1])
       # Total net profit
           net_change = int(row[1]) - previous
           previous = int(row[1])
           net_changes = net_changes +[net_change]
           month = month + [row[0]]
       #greatest increase
           if net_change > greatest_increase[1]:
               greatest_increase[0] = row[0]
               greatest_increase[1] = net_change
       #greatest decrease
           if net_change < greatest_decrease[1]:
               greatest_decrease[0] = row[0]
               greatest_decrease[1] = net_change

       #average net change
           net_monthly_average = sum(net_changes)/len(net_changes)

    #output new txt file
   output = (
       f"\nFinancial Analysis\n"
       f"----------------------------\n"
       f"Total Months:{month_total}\n"
       f"Total: ${total_net_profit}\n"
       f"Average Change: ${net_monthly_average:.2f}\n"
       f"Greatest Increase in Profits: {greatest_increase[0]}(${greatest_increase[1]})\n"
       f"Greatest Decrease in Profits: {greatest_decrease[0]}(${greatest_decrease[1]})\n")


   #Print the data to terminal
   print(output)


   #Export to text file
   with open (newfile, "w") as txt_file:
       txt_file.write(output)