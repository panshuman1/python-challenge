#This file contains Python Module Challenge3
#PyPoll
import os
import csv


budget_csv = os.path.join("..","Resources", "election_data.csv")

#Reading CSV
with open(budget_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    #Skipping the header
    csv_header=next(csv_reader)
    
    #Initializing variables
    rowcount  = 0
    vote_cnt_charles = 0
    vote_cnt_diana = 0
    vote_cnt_raymon = 0
    vote_cnt_others = 0
    vote_per_charles= 0
    vote_per_diana= 0
    vote_per_raymon= 0
    winner=''


    for row in csv_reader:
        rowcount+= 1
        if row[2]=="Charles Casper Stockham":
            vote_cnt_charles+= 1
        elif row[2]=="Diana DeGette" :  
            vote_cnt_diana+= 1
        elif row[2]=="Raymon Anthony Doane" :
            vote_cnt_raymon+= 1
        else:
            vote_cnt_others+= 1  
    #Calculating voting percentage 
    vote_per_charles=round((vote_cnt_charles/rowcount)*100,3)
    vote_per_diana=round((vote_cnt_diana/rowcount)*100,3)
    vote_per_raymon=round((vote_cnt_raymon/rowcount)*100,3)
    
    #determine winner 
    if vote_cnt_charles> vote_cnt_diana and vote_cnt_charles> vote_cnt_raymon:
        winner="Charles Casper Stockham"
    elif  vote_cnt_diana> vote_cnt_charles and vote_cnt_diana> vote_cnt_raymon:  
        winner="Diana DeGette"
    elif vote_cnt_raymon> vote_cnt_charles and vote_cnt_raymon> vote_cnt_charles :  
        winner="Diana DeGette" 


    #Printing results
    print(f"Election Results") 
    print(f"------------------------------------------------------------"+'\n') 
    print(f"Total Votes: {rowcount}") #Printing total votes
    print(f"------------------------------------------------------------"+'\n') 
    print(f"Charles Casper Stockham: {vote_per_charles}% ({vote_cnt_charles})")
    print(f"Diana DeGette: {vote_per_diana}% ({vote_cnt_diana})")
    print(f"Raymon Anthony Doane: {vote_per_raymon}% ({vote_cnt_raymon})")
    print(f"------------------------------------------------------------"+'\n')      
    print(f"Winner: {winner}")