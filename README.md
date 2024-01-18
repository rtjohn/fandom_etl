# Fandom Scraper

This is a tool to scrape and clean the page content from any Fandom.com (e.g. https://harrypotter.fandom.com).

The tool is a modified version of [ScrapeFandom](https://github.com/JOHW85/ScrapeFandom/tree/main) which itself relies heavily upon [WikiExtractor](https://github.com/JOHW85/wikiextractor/tree/master). Those tools are much more full-feature, robust, and set-up to be used as a Python package. I encourage to check them out.

My goal was to produce a smaller, simpler version that could be controlled entirely from the command line.

## Installation

I aimed for ease of installation and a quick time to obtaining files.

1. Clone the repo to a location of your choosing.
2. Source the run-me.sh file with appropriate arguments

## Example Usage

`./run-me.sh all ~/Documents/my_project/ harrypotter`

The above line will run 'all' steps.  The raw, processed, and cleaned file directories will be placed into ~/Documents/my_project/.
The fandom that will be scraped is https://harrypotter.fandom.com

`./run-me.sh 1 ~/scraped_data/ matrix`

The above line will run step 1 only which is scraping.  The raw file directories will be placed into ~/scraped_data/.
The fandom that will be scraped is https://matrix.fandom.com

`./run-me.sh 4 ~/scraped_data/ matrix`

The above line will run step 4 only which is cleaning.  The cleaned file directories will be placed into ~/scraped_data/.
The fandom that will be scraped is https://matrix.fandom.com.  However, in this case the "matrix" argument serves only to complete the path to the files that need to be cleaned: ~/scraped_data/matrix_processed/  

## License
The code is made available under the [GNU Affero General Public License v3.0](LICENSE).