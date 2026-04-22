# Sekai 4koma Downloader

Simple script to grab high-res English comics from Sekaipedia. It automatically skips thumbnails to get the full-quality files and renames them so they stay in order (001, 002, etc.).

## How to use

1. **Install Python**: Make sure you have Python installed.
2. **Install Libraries**: Run this in your terminal/command prompt:
   ```bash
   pip install requests bs4
   ```
3. **Configure**: Open the script and change these two lines:
   * `PAGE`: The URL of the comic range (1-100, 101-200, etc.).
   * `SAVE_DIR`: Where you want the images to go.
4. **Run**: 
   ```bash
   python name_of_script.py
   ```

## Why this exists
* **Full Quality**: It fixes the URLs to bypass the small "thumb" versions.
* **English Only**: Filters for the `_en` versions of the comics.
* **Sorted**: Prepends numbers to the filename so your image viewer doesn't scramble the reading order.
* **Headers**: Uses a User-Agent so the site doesn't immediately kick the script for being a bot.

## Heads up
* **Paths**: If you're on **Windows**, your path should look like `C:/Users/Name/Downloads/Comics`. Use forward slashes `/` even on Windows to avoid issues.
* **Speed**: There is a tiny delay (`time.sleep`) between downloads so the site's server doesn't get annoyed.
