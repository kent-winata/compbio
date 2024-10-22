import csv

max_rise = float('-inf')
previous_water_level = None
previous_date_time = None
max_rise_date_time = None

file_path = 'CO-OPS_8727520_wl.csv'  

with open(file_path, 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        try:
            current_water_level = float(row['Water Level'])
            current_date_time = row['Date Time']
            
            if previous_water_level is not None:
                rise = current_water_level - previous_water_level
                
                if rise > max_rise:
                    max_rise = rise
                    max_rise_date_time = current_date_time
            
            previous_water_level = current_water_level
            previous_date_time = current_date_time
            
        except ValueError:
            continue
            
if max_rise_date_time:
    print(f'Fastest Rise in Water Level: {max_rise} at {max_rise_date_time}')
else:
    print('No valid water level data found.')
