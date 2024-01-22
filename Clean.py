"""
This script cleans text files in a specified directory by applying regex substitutions and writes the cleaned content to a new directory.
"""

import argparse
import re
import os

def clean_scraped_files(file_path, patterns):
    """
    Cleans the provided text file by applying a series of regex substitutions.
    
    :param file_path: Path to the file to be cleaned.
    :param patterns: A list of regex patterns for cleaning the text.
    :return: Cleaned text as a string, or None if an error occurs.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()

        for pattern in patterns:
            text = re.sub(pattern, '', text)

        return text
    except IOError as e:
        print(f"An error occurred: {e}")
        return None

# Argument parsing
parser = argparse.ArgumentParser()
parser.add_argument('input_fandom', help='Fandom\'s name')
parser.add_argument('output_dir', help='Output directory path')
args = parser.parse_args()

# Compile regex patterns
patterns = [r'"id": ',
            r'"revid": ',
            r'"url": ',
            r'"title": ',
            r'"text": ',
            r'"https?://[^\s"]+"',
            r',\s*""',
            r'"\d+"',
            r'[{}]',
            r'&lt;a\shref=\\"[a-zA-Z]+',
            r'a&gt;',
            r'%\d\d',
            r'"&gt;',
            r'&lt;',
            r'\\n',
            r'\\',
            r', , ,', 
            r'\/',
            r'\d\d\d\dDR',
            r'u2022',
            r'href="',
            r'00fb',
            r'\[http:www.amazon.com'
            r'dp0786901187',
            r'Amazon.com',
            r'product page',
            r'! colspan="\d" \|',
            r'! colspan="\d"',
            r'u00ad',
            r'u2014',
            r'!',
            r'="[^"]*"',
            r'u00b7']

def process_directory(source_dir, output_dir, patterns):
    # Ensure the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Process each file in the source directory
    for filename in os.listdir(source_dir):
        file_path = os.path.join(source_dir, filename)
        
        # Check if it's a file and not a directory
        if os.path.isfile(file_path):
            processed_content = clean_scraped_files(file_path, patterns)
            
            # Define the path for the output file
            output_file_path = os.path.join(output_dir, filename)
            
            # Save the processed content to the new file
            with open(output_file_path, 'w') as output_file:
                output_file.write(processed_content)

def find_subdirectories(directory):
    # Find all subdirectories in the given directory
    return [os.path.join(directory, d) for d in os.listdir(directory) if os.path.isdir(os.path.join(directory, d))]

# Define your main directory
# Determine directories for reading and writing files
base_dir = os.path.join(args.output_dir, args.input_fandom + "_processed")
output_subdir = os.path.join(args.output_dir, args.input_fandom + "_cleaned")
os.makedirs(output_subdir, exist_ok=True)

# Full path for the output directory
output_dir = os.path.join(base_dir, output_subdir)

# Find and process each subdirectory
for source_dir in find_subdirectories(base_dir):
    process_directory(source_dir, output_dir, patterns=patterns)