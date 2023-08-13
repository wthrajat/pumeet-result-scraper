![2023-08-13-22:29:46-screenshot](https://github.com/wthrajat/pumeet-result-scraper/assets/38693805/9359ccfc-5132-42d4-a6d8-9efb8955d98b)

## What is this?
See description

## How to use this?
Just run the script & see the output in the console/terminal

### Pre-requisites
1. Selenium `pip install selenium`
2. Webdriver for your browser (Using any `Chromium` based browser is recommended for this):
    - For Chrome, install [chromedriver](https://chromedriver.chromium.org/downloads)
    - For Firefox, install [geckowebdriver](https://github.com/mozilla/geckodriver/releases)

3. Shortcut: if the webdriver isn't installed in the system path, you can just provide its location as:
```python
    driver = webdriver.Chrome("/path/to/webdriver")
    # OR
    driver = webdriver.Firefox("/path/to/webdriver")
```
4. (If you are on Windows, make sure to put `.exe` in the path, i.e., `driver = webdriver.Chrome("/path/to/webdriver.exe")`

5. (Optional) Print to the console or use Pandas library to import this to a python list or whatever to sort it according to the rank.
(Sorted version in `./assets`)

## Why?
Many people wanted to see the Marks vs Rank data for this year's PUMEET

