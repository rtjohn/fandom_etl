import argparse
import re
import os

# The code then does the following:
# 1. Goes to that directory
# 2. Creates a new sister directory with "_cleaned" appended
# 3. Runs cleaned_scraped_files over all files in the original directory
# 4. Writes the cleaned files to the _cleaned directory 

def clean_scraped_files(file_path):
    """
    Cleans the provided text file by applying a series of regex substitutions.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            dirty_text = file.read()
        # Combine multiple regex patterns into fewer steps for efficiency
        patterns = [
            r'"id": ', r'"revid": ', r'"url": ', r'"title": ', r'"text": ',
            r'"https?://[^\s"]+"', r',\s*""', r'"\d+"', r'[{}]',
            r'&lt;a\shref=\\"[a-zA-Z]+', r'a&gt;', r'%\d\d', r'"&gt;', r'&lt;', r'\\n', r'\\',
            r', , ,', r'\/', r'\d\d\d\dDR', r'u2022', r'href="'
        ]
        for pattern in patterns:
            clean_text = re.sub(pattern, '', dirty_text)

        return clean_text
    
    except IOError as e:
        print(f"An error occurred: {e}")
        return None

# Argument parsing
parser = argparse.ArgumentParser()
parser.add_argument('input_fandom', help='Fandom\'s name')
parser.add_argument('output_dir', help='Output directory path')

args = parser.parse_args()

fandom_site = args.input_fandom
output_dir = args.output_dir

target_directory = os.path.join(args.output_dir, args.input_fandom+"_processed")

print(target_directory)

# Go into the directory with the files
# List all the directories in there
directories = [d for d in os.listdir(target_directory) if os.path.isdir(os.path.join(target_directory, d))]

# Create the _cleaned directory
write_directory = os.makedirs(args.output_dir, args.input_fandom+"_cleaned", exist_ok=True)

for d in directories:
    file_path_a = os.path.join(directory_a, filename)
    print(file_path_a)
    processed_content = cleaning_scraped_files(file_path_a)
    # Save the output to directory B
    file_path_b = os.path.join(directory_b, filename)
    with open(file_path_b, 'w') as file:
        file.write(processed_content)





# Go into each of those directories and run clean_scraped_files on each file
# Write those cleaned files out to a new directory


    

# # Ensure directory B exists
# os.makedirs(directory_b, exist_ok=True)

# # Loop over all files in directory A
# 
            
