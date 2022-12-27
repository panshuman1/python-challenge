import os
import csv


budget_csv = os.path.join("Resources", "budget_data.csv")

with open(budget_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    #Skipping the header
    csv_header=next(csv_reader)
    all_months = []
    total = 0 
    average=0
    prev_profit_loss=0
    placeholer_max_val=0
    placeholer_max_month=''
    placeholer_min_val=0
    placeholer_min_month=''

    for row in csv_reader:
            
        prev_profit_loss=-(prev_profit_loss)+int(row[1])
        
        print(row[0],row[1],prev_profit_loss)
       
        if prev_profit_loss > placeholer_max_val:
            placeholer_max_val=prev_profit_loss
            placeholer_max_month=row[0]
        if prev_profit_loss < placeholer_min_val:
           placeholer_min_val=prev_profit_loss
           placeholer_min_month=row[0]   

        prev_profit_loss=int(row[1])
        
        #if row not in all_months and row != 'Date':
            #all_months.append(row[0])
            #total = total+ int(row[1])
            
    ################################
    print (f'(The MAX placeholder value and month is {placeholer_max_val} - {placeholer_max_month})')
    print (f'(The MIN placeholder value and month is {placeholer_min_val} - {placeholer_min_month})')

    ###############################
    #average= total/len(all_months)
    #print(all_months) 
    #print(f"Financial Analysis") 
    #print(f"****************************************************"+'\n') 
     
    #print(f"Total Months: {len(all_months)}")
    #print(f"Net profit and Loss: ${total}")
    #print(f"Average Change: ${average}")
    