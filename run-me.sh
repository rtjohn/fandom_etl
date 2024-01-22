#!/bin/bash

# Updated usage instructions
# To run only Step 1: ./run-me.sh 1 /path/to/directory harrypotter lordoftherings
# To run only Step 2: ./run-me.sh 2 /path/to/directory harrypotter lordoftherings
# To run only Step 3: ./run-me.sh 3 /path/to/directory harrypotter lordoftherings
# To run all steps: ./run-me.sh all /path/to/directory harrypotter lordoftherings

# Check if values are provided (now expecting at least 3 arguments)
if [ $# -lt 3 ]; then
    echo "Usage: $0 <step> <directory path> <values>"
    echo "Available steps: 1 (Step 1), 2 (Step 2), 3 (Step 3), 4 (Step 4), all (All steps)"
    exit 1
fi

# Get the step and directory path arguments
step="$1"
dir_path="$2"
fandom="$3"
#shift 2

# Loop through the values and run the commands for each value
for f in "$3"; do
    echo "--------------------------------------------------"
    echo "Processing: $value"
    echo "--------------------------------------------------"

    # Check the step argument and execute the corresponding step
    if [ "$step" = "1" ] || [ "$step" = "all" ]; then
        # Step 1: Run Python script to scrape fandom with directory path
        echo "Step 1: Scraping data for $fandom into $dir_path..."
        python3 ScrapeFandom.py "$fandom" "$dir_path"
        echo "Scraping completed for $fandom."
    fi

    if [ "$step" = "2" ] || [ "$step" = "all" ]; then
        # Step 2: Run wikiextractor with necessary options

        # This script seems to be removing tables from content.  This sometimes leaves pages empty
        echo "Step 2: Extracting data from $fandom.xml..."
        python3 WikiExtractor.py "$fandom.xml" "$dir_path" --no-templates -l --json -o "$fandom"
        echo "Data extraction completed for $fandom.xml."
    fi

    if [ "$step" = "3" ] || [ "$step" = "all" ]; then
        # Step 3: Run Python script to convert JSON to text
        echo "Step 3: Converting JSON to JSONL format for $fandom..."
        python3 Json2jsonl.py "$dir_path" "$fandom.jsonl" "$fandom"
        echo "Conversion to JSONL completed for $fandom."
    fi

    if [ "$step" = "4" ] || [ "$step" = "all" ]; then
        # Step 4: Run Python script to convert JSON to text
        echo "Step 4: Cleaning the files from $fandom..."
        python3 Clean.py "$fandom" "$dir_path"
        echo "Cleaning of files is done for $fandom."
    fi
    
done

echo "--------------------------------------------------"
echo "All selected processing steps completed for $fandom."
echo "--------------------------------------------------"
