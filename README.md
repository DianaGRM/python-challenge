# python-challenge

## Description: 

Each Python assignment has the "main.py" which is the script and also inside the "analysis folder" is the txt file with the requested results.
All the documents were uploaded with git bash.

PyBank assignment:
 1) I opened the csv file and skipped the header.
 2) with a counter "x" I counted the data as it passed thru the "for" 
 3) in the variable total I added the amounts of each row as the for loop runs
 4) created a list with the amounts "Profit_loss" and a list with the dates "Dates" for further actions
 5) with a "for" and the amounts list I calculated the difference of each row with the one above and stored it in a new list "profits"
 6) with the information of the past loop, I calculated the average
 7) for the greatest decrease and increase, I made a loop and used the new list "profits" to compare the amounts with an if 
 8) finally I printed all the information as requested and created the txt file. 

PyPoll assignment:
 1) I opened the csv file and skipped the header.
 2) with a counter "x" I counted the data as it passed thru the "for"
 3) Created a new list of all the information in column 3 for further proposes "completelist"
 4) with an "if" I identified the different candidates in all the data and stored them in a list "listcandidates"
 5) with the two lists above and using a "for loop" and "ifs", I calculated the number of votes for each candidate and the %
 6) created a new list with the total of votes for each candidate so it will be easier to compare them and get the winner and the index 
 7) finally I printed all the information as requested and created the txt file. 
