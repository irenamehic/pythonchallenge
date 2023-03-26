##Your task is to create a Python script that analyzes the records to calculate each of the following values:

#The total number of months included in the dataset

#The net total amount of "Profit/Losses" over the entire period

#The changes in "Profit/Losses" over the entire period, and then the average of those changes

#The greatest increase in profits (date and amount) over the entire period

#The greatest decrease in profits (date and amount) over the entire period

import os
import csv

budget_data_csv = os.path.join("/Desktop/pythonchallenge/PyBank/Resources/budget_data.csv")
csv_path_output = ("/Desktop/pythonchallenge/PyBank/Resources/budget_data.txt")

##Setting up the variables
total_months = 0
total_proft_loss = 0
prev_profit_loss = 0
profit_loss_change = 0
greatest_increase = ["",0]
greatest_decrease = ["",9999999]

profit_loss_changes = []

##Read the csv file
with open(csvpath) as csvfile:
    reader = csv.DictReader(csvfile)
    
        for row in reader:
            total_months = total_months + 1
            total_proft_loss = total_profit_loss + int(row["Profit/Losses"])
            print(row)
            
            profit_loss_change = int(row["Profit/Losses"]) - prev_profit_loss
            print(profit_loss_change)
            
            prev_profit_loss = int(row["Profit/Losses"])
            print(prev__profit_loss)
            
            if (profit_loss_change > greatest_increase[1]):
                greatest_increase[1] = profit_loss_change
                greatest_increase[0] = row["Date"]
            if(profit_loss_change < greatest_decrease[1]):
                greatest_decrease[1] = profit_loss_change
                greatest_decrease[0] = row["date"]
                
            profit_loss_changes.append(int(row["profit/Losses"]))
            
        profit_loss_avg = sum(profit_loss_changes) / len(profit_loss_changes)
        
        #Print the output
        
        print("Financial Analysis")
        print("----------------------------")
        print("Total Months': " +str(total_months))
        print("Total : " + "$" + str(total_profit_loss))
        print("Average Change: " + "$" + str(round(sum(profit_loss_changes) / len(profit_loss_changes),2)))
    print("Greatest Increase: " + str(greatest_increase[0]) + " ($" +  str(greatest_increase[1]) + ")") 
    print("Greatest Decrease: " + str(greatest_decrease[0]) + " ($" +  str(greatest_decrease[1]) + ")")
    
    
with open(csvpath_output, "w") as txt_file
    txt_file.write("Total Months: " + str(total_months))
     txt_file.write("\n")
    txt_file.write("Total: " + "$" + str(total_profit_loss))
    txt_file.write("\n")
    txt_file.write("Average Change: " + "$" + str(round(sum(profit_loss_changes) / len(profit_loss_changes),2)))
    txt_file.write("\n")
    txt_file.write("Greatest Increase: " + str(greatest_increase[0]) + " ($" + str(greatest_increase[1]) + ")") 
    txt_file.write("\n")
    txt_file.write("Greatest Decrease: " + str(greatest_decrease[0]) + " ($" + str(greatest_decrease[1]) + ")")