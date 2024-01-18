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
shift 2

# Loop through the values and run the commands for each value
for value in "$@"; do
    echo "--------------------------------------------------"
    echo "Processing: $value"
    echo "--------------------------------------------------"

    # Check the step argument and execute the corresponding step
    if [ "$step" = "1" ] || [ "$step" = "all" ]; then
        # Step 1: Run Python script to scrape fandom with directory path
        echo "Step 1: Scraping data for $value into $dir_path..."
        python3 ScrapeFandom.py "$value" "$dir_path"
        echo "Scraping completed for $value."
    fi

    if [ "$step" = "2" ] || [ "$step" = "all" ]; then
        # Step 2: Run wikiextractor with necessary options
        echo "Step 2: Extracting data from $value.xml..."
        python3 WikiExtractor.py "$value.xml" "$dir_path" --no-templates -l --json -o "$value"
        echo "Data extraction completed for $value.xml."
    fi

    if [ "$step" = "3" ] || [ "$step" = "all" ]; then
        # Step 3: Run Python script to convert JSON to text
        echo "Step 3: Converting JSON to JSONL format for $value..."
        python3 Json2jsonl.py "$value/" "$value.jsonl"
        echo "Conversion to JSONL completed for $value."
    fi

    if [ "$step" = "4" ] || [ "$step" = "all" ]; then
        # Step 4: Run Python script to convert JSON to text
        echo "Step 4: Cleaning the files from $value..."
        python3 Clean.py "$value" "$dir_path"
        echo "Cleaning of files is done for $value."
    fi

    echo "All processing steps completed for $value."
done

echo "--------------------------------------------------"
echo "Processing completed for all provided values."
echo "--------------------------------------------------"
