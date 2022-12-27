#This file contains Python Module Challenge3
#PyBank

import os
import csv

budget_csv = os.path.join("..","Resources", "budget_data.csv")

with open(budget_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    #Skipping the header
    csv_header=next(csv_reader)
    all_months = []
    total = 0 

    #Variable Initialization
    #------------------
    prev_profit_loss=0
    placeholer_max_val=0
    placeholer_max_month=''
    placeholer_min_val=0
    placeholer_min_month=''
    previous_val=0
    curr_val=0
    average_val=0
    #------------------
    
    #Looping through CSV 
    for row in csv_reader:
        if row not in all_months and row != 'Date':
            all_months.append(row[0])
            total = total+ int(row[1])
        
        prev_profit_loss=-(prev_profit_loss)+int(row[1])
        
        #print(row[0],row[1],prev_profit_loss)
       
       #Calculating profit/loss increase/decrease
        if prev_profit_loss > placeholer_max_val:
            placeholer_max_val=prev_profit_loss
            placeholer_max_month=row[0]
        if prev_profit_loss < placeholer_min_val:
           placeholer_min_val=prev_profit_loss
           placeholer_min_month=row[0]   

        prev_profit_loss=int(row[1])
        

        #Calculating Average
        if  previous_val==0:
            previous_val = int(row[1])
        else:   
            curr_val+=int(row[1])-previous_val
            previous_val = int(row[1]) 
        
    average_val= round(curr_val/len(all_months),2)
    #Printing Results
    print(f"Financial Analysis") 
    print(f"-------------------------------------------------------------"+'\n') 
     
    print(f"Total Months: {len(all_months)}")
    print(f"Total: ${total}")
    print(f"Average Change: {average_val} ")

    print (f'Greatest Increase in Profits: {placeholer_max_month} (${placeholer_max_val})')
    print (f'Greatest Decrease in Profits: {placeholer_min_month} (${placeholer_min_val})')
