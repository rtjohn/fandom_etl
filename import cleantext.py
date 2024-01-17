from cleantext import clean

example_text = 'This is A s$ample !!!! tExt3% to   cleaN566556+2+59*/133'

file_path = '/Users/ryanjohnson/Documents/work/fandom_scraper/wikiextractor/ScrapeFandom/forgottenrealms/AA/wiki_00_short' # Replace with your file path
with open(file_path, 'r', encoding='utf-8') as file:
    content = file.read()

print(clean(text=content,
            fix_unicode=True,
            to_ascii=True,
            lower=True,
            no_line_breaks=False,
            no_urls=False,
            no_emails=False,
            no_phone_numbers=False,
            no_numbers=False,
            no_digits=False,
            no_currency_symbols=False,
            no_punct=False,
            replace_with_punct="",
            replace_with_url="This is a URL",
            replace_with_email="Email",
            replace_with_phone_number="",
            replace_with_number="123",
            replace_with_digit="0",
            replace_with_currency_symbol="$",
            lang="en"
            ))