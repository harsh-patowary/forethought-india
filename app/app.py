# from bcrypt import requests
import requests
from flask import Flask, render_template, request, url_for, flash, redirect
from bs4 import BeautifulSoup
import cycler
import extractor

app = Flask(__name__)
# cycler_obj = cycler.cycle()
extractor_obj = extractor.extract()


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("index.html")


def mop_up():
    urls = set()
    urls = url_cycling()
    emails = []
    for url in urls:
        
        emails = extractor_obj.email_extracting(url)
        extractor_obj.write_file(emails, url)
        if(len(emails)>0):
            # print(emails)
            print("**Crawl Successfull**")

        else:
            print(f"+Empty Link+ {url}+")
            print(f"Empty links are links with null extracts")


def url_cycling(self):
        url = input("Enter the base URL: ")
        reqs = requests.get(url)
        soup = BeautifulSoup(reqs.text, 'lxml')

        # file = open("/home/kali/scripts/mop-up/data/urls.csv", "w")

        urls = set()
        urls.add(url)
        print(urls)
        for link in soup.find_all('a'):
            urls.add(link.get('href'))

        return urls
