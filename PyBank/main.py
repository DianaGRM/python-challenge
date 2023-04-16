import csv
import os
x = 0
total = 0
sumdif = 0
increase = 0
decrease = 0


Profit_loss=[]
Profits = []
Dates = []

csvpath = os.path.join("Resources", "budget_data.csv")

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile)
    
    csv_header = next(csvreader)

    for row in csvreader:
        x = x + 1
        total = total + int(row[1])
        
        #stores the dates and the amounts in differents lists 
        Profit_loss.append(row[1])
        Dates.append(row[0])
        
    

    
#loop for getting the changes and the average of the profit/losses
    for k in range(1,86):
        j=k-1
        #dif -> Changes in Profit/Losses
        dif = int(Profit_loss[k]) - int(Profit_loss[j])

        #stores the changes in a new list
        Profits.append(dif)

        sumdif =  sumdif + dif 

    average = round(sumdif/85,2)

    #loop for the greatest increase and decrease
    for z in range(84):
     if int(Profits[z]) > increase:
            increase = int(Profits[z])
            datei = z + 1 
        
     if int(Profits[z]) < decrease:
            decrease = int(Profits[z])
            dated = z + 1
    
    #Final print 
    print("Financial Analysis \n")
    print("-------------------------------- \n")
    print(f"Total Months: {x} \n")
    print(f"Total: ${total}\n")
    print(f"Average Change: ${average}\n")
    print(f"Greatest Increase in Profits: {Dates[datei]} (${increase})\n")
    print(f"Greatest Decrease in Profits: {Dates[dated]} (${decrease})")

    #creating the txt file 
    file = open("analysis/Results.txt","w")
    file.write("Financial Analysis \n")
    file.write("-------------------------------- \n")
    file.write(f"Total Months: {x} \n")
    file.write(f"Total: ${total}\n")
    file.write(f"Average Change: ${average}\n")
    file.write(f"Greatest Increase in Profits: {Dates[datei]} (${increase})\n")
    file.write(f"Greatest Decrease in Profits: {Dates[dated]} (${decrease})")


     


    