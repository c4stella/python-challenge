#Importing os module
import os
#Importing csv module
import csv

#Obtaining current working directory
cwd = os.getcwd()
#print(cwd)

#Setting file path of desired csv file
csvpath = os.path.join(cwd, 'Resources', 'election_data.csv')
#print(csvpath)

#Setting file path of results file
respath = os.path.join(cwd, 'Analysis', 'results.txt')

#Setting default values for variables
voteList = []
indCountList = []
count = {}

#Reading csv file
with open(csvpath, encoding='UTF8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #print(csvreader)
    
    #Skips the header row
    next(csvreader)
    #print(csvreader)
    
    #Loop through all rows in the csv file
    for row in csvreader:
        #print(row)
        
        #Append all candidate votes (and their names) to list
        voteList.append(row[2])

    #Change list into set (which does not allow duplicate values) and then changes back into list
    allCand = list(set(voteList))
    
    #Loop through all elements in list allCand, which has all unique candidates
    for i in range(len(allCand)):
        
        #Set variable to a candidate's name
        uniqueCand = allCand[i]
        #Append the total instances that a candidate's name appeared in the total votes
        indCountList.append(voteList.count(uniqueCand))
        #Sort candidates and their total votes with each other in dictionary
        count[uniqueCand] = indCountList[i]
        
        #Find the largest value
        mostVoted = max(count.values())
        #Find the key associated with the largest value
        winner = list(count.keys())[list(count.values()).index(mostVoted)]
        
#print(len(voteList)) #== 369711
#print(allCand) #== ['Raymon Anthony Doane', 'Charles Casper Stockham', 'Diana DeGette']
#print(indCountList) #== [11606, 85213, 272892]

#Set variable for all votes cast
totalVotes = len(voteList)

#Structuring results
vresult = f'''
```text
Election Results
-------------------------
Total Votes: {totalVotes}
-------------------------
{allCand[0]}: {round(((indCountList[0]/totalVotes) * 100), 3)}% ({indCountList[0]})
{allCand[1]}: {round(((indCountList[1]/totalVotes) * 100), 3)}% ({indCountList[1]})
{allCand[2]}: {round(((indCountList[2]/totalVotes) * 100), 3)}% ({indCountList[2]})
-------------------------
Winner: {winner}
-------------------------
```
'''

#Export output as its own txt file
print(vresult, file=open(respath, 'w'))