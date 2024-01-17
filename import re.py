import re
import os

def cleaning_shit(file_path):
    # Real world
    with open(file_path, 'r', encoding='utf-8') as file:
        dirty_text = file.read()
    # Need to fix this ugly shit
    step1 = re.sub(r'"id": ', '', dirty_text)
    step2 = re.sub(r'"revid": ', '', step1)
    step3 = re.sub(r'"url": ', '', step2)
    step4 = re.sub(r'"title": ', '', step3)
    step5 = re.sub(r'"https?://[^\s"]+"', '', step4)
    step6 = re.sub(r'"text": ', '', step5)
    step7 = re.sub(r',\s*""', '', step6)
    step8 = re.sub(r'"\d+"', '', step7)
    step9 = re.sub(r'[{}]', '', step8)
    step10 = re.sub(r'&lt;a\shref=\\"[a-zA-Z]+','', step9)
    step11 = re.sub(r'a&gt;','', step10)
    step12 = re.sub(r'%\d\d','', step11)
    step13 = re.sub(r'"&gt;','', step12)
    step14 = re.sub(r'&lt;','', step13)
    step15 = re.sub(r'\\n','', step14)
    step16 = re.sub(r'\\','', step15)
    step17 = re.sub(r', , ,','', step16)
    step18 = re.sub(r'\/','', step17)
    step19 = re.sub(r'\d\d\d\dDR','', step18)
    step20 = re.sub(r'u2022','', step19)
    step21 = re.sub(r'href="','', step20)
    return step21
    
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
            
