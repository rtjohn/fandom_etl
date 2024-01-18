import requests
from bs4 import BeautifulSoup
import argparse
from tqdm import tqdm
import errno, os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc:
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise

def safe_open_w(path):
    ''' Open "path" for writing, creating any parent directories as needed. '''
    mkdir_p(os.path.dirname(path))
    return open(path, 'wb')

# Sets up Chrome WebDriver options for headless browsing
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("disable-infobars")
chrome_options.add_argument('--disable-extensions')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--no-sandbox')

# Argument parsing
parser = argparse.ArgumentParser()
parser.add_argument('input_fandom', help='Fandom\'s name')
parser.add_argument('output_dir', help='Output directory path')
args = parser.parse_args()

fandom_site = args.input_fandom
output_dir = args.output_dir

# Check if the directory exists and create if it does not
mkdir_p(output_dir)
mkdir_p(os.path.join(output_dir, f"{fandom_site}_raw"))

# Start scraping process
nextpage_url = "/wiki/Special:AllPages"
AllPage = f"https://{fandom_site}.fandom.com{nextpage_url}"
counter = 0

while nextpage_url != "":
    listofpages = ""
    try:
        req = requests.get(AllPage, allow_redirects=False)
        if req.content != b'':
            soup = BeautifulSoup(req.content, "lxml")
            content = soup.find("div", {"class": "mw-allpages-body"})
            nextpage = soup.find("div", {"class": "mw-allpages-nav"})
        else:
            driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
            driver.get(AllPage)
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            content = soup.find("div", {"class": "mw-allpages-body"})
            nextpage = soup.find("div", {"class": "mw-allpages-nav"})
            driver.quit()

        if content:
            listofentries = content.find_all("li")
            for i in tqdm(listofentries, desc=f"Scraping {AllPage}"):
                listofpages += i.text.replace("(redirect", "") + "\n"
            
            payload = {'catname': '', 'pages': listofpages, 'curonly': '1', 'wpDownload': 1, 'wpEditToken': '+\\', 'title': 'Special:Export'}
            response = requests.post(f"https://{fandom_site}.fandom.com/wiki/Special:Export", data=payload)
            data = response.content

            with safe_open_w(os.path.join(output_dir, f"{fandom_site}_raw", f"{counter}.xml")) as f:
                f.write(data)
            counter += 1
        else:
            print("No content found")

        if nextpage:
            nav = nextpage.findAll("a")
            if len(nav) > 0 and "Next page" in nav[-1].text:
                nextpage_url = nav[-1]["href"]
                AllPage = f"https://{fandom_site}.fandom.com{nextpage_url}"
            else:
                nextpage_url = ""
        else:
            break
    except Exception as e:
        print("Error", e)
        continue

# Combine all XML files into one
files = os.listdir(os.path.join(output_dir, f"{fandom_site}_raw"))
with open(os.path.join(output_dir, f"{fandom_site}.xml"), "w") as outfile:
    for fname in files:
        with open(os.path.join(output_dir, f"{fandom_site}_raw", fname), "r") as infile:
            outfile.write(infile.read())
            outfile.write("\n")
