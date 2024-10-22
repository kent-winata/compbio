import csv

highest_water_level = float('-inf')
lowest_water_level = float('inf')
total_water_level = 0
count = 0

highest_date_time = None
lowest_date_time = None

file_path = 'CO-OPS_8727520_wl.csv'  

with open(file_path, 'r') as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        try:
            # Read the water level as a float
            water_level = float(row['Water Level'])
            
            total_water_level += water_level
            count += 1
            
            if water_level > highest_water_level:
                highest_water_level = water_level
                highest_date_time = row['Date Time']
            
            if water_level < lowest_water_level:
                lowest_water_level = water_level
                lowest_date_time = row['Date Time']
                
        except ValueError:
            continue

# Calculate the average water level
if count > 0:
    average_water_level = total_water_level / count
else:
    average_water_level = None

# After reading the file, print the lowest, highest, and average water levels
if highest_date_time and lowest_date_time:
    print(f'Highest Water Level: {highest_water_level} at {highest_date_time}')
    print(f'Lowest Water Level: {lowest_water_level} at {lowest_date_time}')
    print(f'Average Water Level: {average_water_level:.2f}')
else:
    print('No valid water level data found.')
