import re

# This should be one function that take sthe following arguments:
# 1. A path to a directory of scraped files that needs to be cleaned

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
    
# Directories
directory_a = '/Users/ryanjohnson/Documents/work/fandom_scraper/wikiextractor/ScrapeFandom/forgottenrealms/AA'
directory_b = '/Users/ryanjohnson/Documents/work/fandom_scraper/wikiextractor/ScrapeFandom/forgottenrealms/AA_clean'

# Ensure directory B exists
os.makedirs(directory_b, exist_ok=True)

# Loop over all files in directory A
for filename in os.listdir(directory_a):
    file_path_a = os.path.join(directory_a, filename)
    print(file_path_a)
    processed_content = cleaning_shit(file_path_a)
    # Save the output to directory B
    file_path_b = os.path.join(directory_b, filename)
    with open(file_path_b, 'w') as file:
            file.write(processed_content)
            
