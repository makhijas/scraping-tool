from pymongo import MongoClient
from bson.objectid import ObjectId
client = MongoClient("mongodb://localhost:27017/")
scraped_db = client.scraped_from_web ##database called scraped_from_web
raw_website_data = scraped_db.raw_website_data ##collection called raw_website_data
import requests
from bs4 import BeautifulSoup
def scrape_site(url: str) -> bytes:
    r = requests.get(url)
    data = r.content
    raw_website_data.insert_one({"url": url, "data": data }) ##collection dictionary ##used insert_one to store data
    raw_website_data.find_one("url")
    print (type(raw_website_data[url]))
    #website_data_soup = BeautifulSoup(r.content, "html.parser")
    #print(website_data_soup.prettify())
    #print(website_data_soup.prettify())
scrape_site("https://api.mongodb.com/python/current/tutorial.html")
def check_url(url: str) -> bytes:
    for website_url in raw_website_data.find():
        if raw_website_data[website_url] == website_url:
            return raw_website_data["data"]
        else:
            raw_website_data.insert_one({"url": website_url, "data": data })
            return raw_website_data["data"]

check_url("https://api.mongodb.com/python/current/tutorial.html")
