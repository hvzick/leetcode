




import os

# List all files in the directory
files = [f for f in os.listdir() if f[0].isdigit()]  # Filter files starting with digits

for file in files:
    num_part = ''.join(filter(str.isdigit, file))  # Extract numeric part
    rest = file[len(num_part):]  # Extract the remaining filename part
    new_name = f"{int(num_part):04d}{rest}"  # Format with leading zeros (4-digit)
    
    os.rename(file, new_name)
    print(f"Renamed: {file} -> {new_name}")









# 2 26
# 280
# 4213630015305823