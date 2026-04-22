import os
import requests
from bs4 import BeautifulSoup
import time

PAGE = ("https://www.sekaipedia.org/wiki/SEKAI_no_4koma_(1-100)") #Can only be 1-100, 101-200, 201-300, 301-400, anything beyond won't work
SAVE_DIR = os.path.expanduser("..") #Set your own path
HEADERS = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36"} #copy user agent data here:


def download_all_sekai():
    if not os.path.exists(SAVE_DIR):
        os.makedirs(SAVE_DIR)

    print("Fetching page indices...")
    res = requests.get(PAGE, headers=HEADERS)
    soup = BeautifulSoup(res.text, 'html.parser')

    all_imgs = soup.find_all('img')

    unique_links = set()
    for img in all_imgs:
        src = img.get('src') or img.get('data-src')
        if not src: continue

        if "static.wikitide.net" in src and "_en." in src.lower():

            clean_url = src
            if "/thumb/" in clean_url:
                clean_url = clean_url.replace("/thumb/", "/")
                clean_url = "/".join(clean_url.split("/")[:-1])

            unique_links.add(clean_url)

    sorted_links = sorted(list(unique_links))
    print(f"Found {len(sorted_links)} high-res English comics. Starting download...")

    for i, url in enumerate(sorted_links):
        try:
            if url.startswith("//"):
                url = "https:" + url

            img_res = requests.get(url, headers=HEADERS, timeout=15)
            if img_res.status_code == 200:
                filename = url.split('/')[-1]
                save_name = f"{i + 1:03d}_{filename}"

                with open(os.path.join(SAVE_DIR, save_name), 'wb') as f:
                    f.write(img_res.content)
                print(f"[{i + 1}/{len(sorted_links)}] Saved: {save_name}")
            else:
                print(f"Skipped (Error {img_res.status_code}): {url}")

            time.sleep(0.1)  # be a good netizen
        except Exception as e:
            print(f"Failed on {url}: {e}")


if __name__ == "__main__":
    download_all_sekai()