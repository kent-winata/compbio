import csv

previous_water_level = None
previous_date_time = None

file_path = 'CO-OPS_8727520_wl.csv' 

with open(file_path, 'r') as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        try:
            current_water_level = float(row['Water Level'])
            current_date_time = row['Date Time']
            
            if previous_water_level is not None:
                if current_water_level - previous_water_level > 0.25:
                    print(f'WARNING: Water level increased by more than 0.25 at {current_date_time}. Previous: {previous_water_level}, Current: {current_water_level}')
            
            if current_water_level > 5.0:
                print(f'WARNING: Water level exceeded 5.0 at {current_date_time}. Current: {current_water_level}')
            
            previous_water_level = current_water_level
            previous_date_time = current_date_time
        
        except ValueError:
            if previous_date_time:
                print(f'WARNING: No reading received at {previous_date_time}')
          
            previous_water_level = None
            continue
