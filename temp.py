import requests
import selectorlib
from datetime import datetime
import sqlite3

URL = "http://programmer100.pythonanywhere.com/"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

connection = sqlite3.connect("temp.db")
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
    row = extracted.split(",")
    row = [item.strip() for item in row]
    cursor = connection.cursor()
    cursor.execute("INSERT INTO temperatura VALUES(?,?)", (now, extracted))
    connection.commit()


if __name__ == "__main__":
    scraped = scrape(URL)
    extracted = extract(scraped)
    store(extracted)
    print(extracted)


