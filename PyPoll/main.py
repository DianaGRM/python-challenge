import os
import csv
x=0
votesC = 0
votesD = 0
votesR = 0

completelist = []
listcandidates = []

csvpath = os.path.join("Resources","election_data.csv")

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile) 

    csv_header = next(csvreader)

    for row in csvreader:
        #Total votes
        x = x + 1

        #list of candidates 
        completelist.append(row[2])
        if row[2] not in listcandidates:
            
            listcandidates.append(row[2])

    for can in completelist:
        #counting the votes for each candidate
        if can == listcandidates[0]:
            votesC = votesC + 1

        if can == listcandidates[1]:
            votesD = votesD + 1
        
        if can == listcandidates[2]:
            votesR = votesR + 1
    

    #percentage of vote of each candidate 

    perC = round((votesC/x)*100,3)
    perD = round((votesD/x)*100,3)
    perR = round((votesR/x)*100,3)
    

    #winner
    listvotes = [votesC,votesD,votesR]
    a = 0
    for v in listvotes:
        if v > a:
         a = v
         ind = listvotes.index(a)
    
    #Final Print 

    print("Election Results\n")
    print("--------------------------------\n")
    print(f"Total Votes: {x}\n")
    print("--------------------------------\n")
    print(f"{listcandidates[0]}: {perC}% ({votesC})\n")
    print(f"{listcandidates[1]}: {perD}% ({votesD})\n")
    print(f"{listcandidates[2]}: {perR}% ({votesR})\n")
    print("--------------------------------\n")
    print(f"Winner: {listcandidates[ind]}\n")
    print("--------------------------------\n")
    
    #creating the txt file
    
    file = open("analysis/Results.txt","w")
    file.write("Election Results\n")
    file.write("--------------------------------\n")
    file.write(f"Total Votes: {x}\n")
    file.write("--------------------------------\n")
    file.write(f"{listcandidates[0]}: {perC}% ({votesC})\n")
    file.write(f"{listcandidates[1]}: {perD}% ({votesD})\n")
    file.write(f"{listcandidates[2]}: {perR}% ({votesR})\n")
    file.write("--------------------------------\n")
    file.write(f"Winner: {listcandidates[ind]}\n")
    file.write("--------------------------------\n")
        