import csv

highest_water_level = float('-inf')
highest_date_time = None

file_path = 'CO-OPS_8727520_wl.csv'

with open(file_path, 'r') as file:
    # reading file
    reader = csv.DictReader(file)
    
    # reading each row
    for row in reader:
        try:
            # Read the water level as a float
            water_level = float(row['Water Level'])
            
            # Check if this is the highest water level encountered so far
            if water_level > highest_water_level:
                highest_water_level = water_level
                highest_date_time = row['Date Time']
        except ValueError:
            # Skipping rows if there are invalids
            continue

# After reading the file, print the highest water level and the corresponding date and time
if highest_date_time:
    print(f'Highest Water Level: {highest_water_level} at {highest_date_time}')
else:
    print('No valid water level data found.')
