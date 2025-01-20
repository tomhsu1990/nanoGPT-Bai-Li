import os
import requests
from bs4 import BeautifulSoup
from opencc import OpenCC
from requests.exceptions import RequestException, ChunkedEncodingError
import re

# Initialize OpenCC for Simplified to Traditional Chinese translation
cc = OpenCC('s2t')

def fetch_and_parse_poems(base_url, output_file):
    poems = []

    # Fetch the first page to determine the number of pages
    try:
        response = requests.get(f"{base_url}.html", timeout=10)
        response.encoding = 'utf-8'  # Ensure proper encoding
        response.raise_for_status()
    except RequestException as e:
        print(f"Error fetching {base_url}.html: {e}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the pagination to loop through all pages
    pagination = soup.find("div", class_="pagination")
    last_page = int(pagination.find_all("a")[-2].text) if pagination else 1

    for page in range(1, last_page + 1):
        page_url = f"{base_url}_{page}.html" if page > 1 else f"{base_url}.html"
        print(f"Fetching: {page_url}")

        try:
            response = requests.get(page_url, timeout=10)
            response.encoding = 'utf-8'  # Ensure proper encoding
            response.raise_for_status()
        except RequestException as e:
            print(f"Error fetching {page_url}: {e}. Skipping.")
            continue

        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all poem entries (content links)
        for h3 in soup.find_all('h3'):
            title_tag = h3.find('a')

            if title_tag:
                poem_url = f"{base_url.rsplit('/', 1)[0]}/{title_tag['href']}"
                print(f"Fetching poem: {poem_url}")

                try:
                    poem_response = requests.get(poem_url, timeout=10)
                    poem_response.encoding = 'utf-8'
                    poem_response.raise_for_status()
                except (RequestException, ChunkedEncodingError) as e:
                    print(f"Error fetching {poem_url}: {e}. Skipping.")
                    continue

                poem_soup = BeautifulSoup(poem_response.text, 'html.parser')

                # Extract poem content
                content_div = poem_soup.find("div", class_="shici-content")
                if content_div:
                    content = content_div.get_text(separator="\n").strip()
                    if not re.search(r'\（(.*?\）)|\[.*?\]|●|【.*?】', content):
                        content_traditional = cc.convert(content)
                        poems.append(content_traditional)

    # Write the poems to the output file
    with open(output_file, 'w', encoding='utf-8') as f:
        for content in poems:
            f.write(f"{content}\n\n")

    print(f"Poems successfully saved to {output_file}")

if __name__ == "__main__":
    base_url = "http://www.yiduiyi.net.cn/chaxun/zuozhe/1"  # Base URL of the first page
    output_file = "input.txt"

    fetch_and_parse_poems(base_url, output_file)
