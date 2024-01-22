"""
This script converts JSON files from a specified directory to a JSON Lines format,
writing the output to a single file. It also cleans and reformats the JSON data.
"""

import json
import os
import re
import argparse
from tqdm import tqdm

def clean_text(text, url_regex):
    """
    Clean the text by removing URLs and performing other standardizations.

    :param text: The text to clean.
    :param url_regex: Compiled regex pattern to match URLs.
    :return: Cleaned text.
    """
    text = re.sub(url_regex, r'\2', text)
    text = re.sub(r'\(\s+', '(', text)
    return text.replace('()', '').replace("\u00a0", " ").replace(" , ", ", ")

# Argument parsing
parser = argparse.ArgumentParser()
parser.add_argument('input_dir', help='Directory with wiki json files')
parser.add_argument('output', help='Txt file output')
parser.add_argument('fandom_dir', help='Name of fandom')
args = parser.parse_args()

source_directory = os.path.join(args.input_dir, args.fandom_dir + "_processed")


# Compile URL regex pattern
url_regex = re.compile(r'&lt;a href="(.*?)"&gt;(.*?)&lt;/a&gt;')

# Process files and write output
counter = 0
with open(args.output, 'w') as fout:
    for directory in tqdm(os.listdir(source_directory), desc="Directories"):
        dir_path = os.path.join(source_directory, directory)
        if os.path.isdir(dir_path):
            for filename in tqdm(os.listdir(dir_path), desc=f"Processing {directory}"):
                if not filename.startswith('wiki'):
                    continue

                path = os.path.join(dir_path, filename)
                with open(path, 'r') as fin:
                    for line in fin:
                        data = json.loads(line)
                        if data['text'] == "":
                            continue

                        title = "#" + data['title'] + "\n"
                        text = clean_text(data['text'], url_regex)
                        output_json = {
                            "meta": data["url"],
                            "text": title + text
                        }
                        fout.write(json.dumps(output_json) + '\n')
                        counter += 1

print(f"Total processed entries: {counter}")
