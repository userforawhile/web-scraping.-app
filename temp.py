import requests
import selectorlib
from datetime import datetime

URL = "http://programmer100.pythonanywhere.com/"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


def scrape(url):
    """scrape the source page form the url"""
    response = requests.get(url, headers=HEADERS)
    source = response.text
    return source


def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("ext.yaml")
    value = extractor.extract(source)["temp"]
    return value


def store(extracted):
    now = datetime.now().strftime("%y-%m-%d-%H %M %S")
    with open("data1.txt", "a") as file:
        line = f"{now}, {extracted}\n"
        file.write(line)


if __name__ == "__main__":
    scraped = scrape(URL)
    extracted = extract(scraped)
    store(extracted)
    print(extracted)


