import requests
from flask import Flask, render_template, request, url_for, flash, redirect
import os
from bs4 import BeautifulSoup

class cycle:

    

    def url_cycling(self, l):
        url = l
        reqs = requests.get(url)
        soup = BeautifulSoup(reqs.text, 'lxml')

        # file = open("/home/kali/scripts/mop-up/data/urls.csv", "w")

        urls = set()
        urls.add(url)
        print(urls)
        for link in soup.find_all('a'):
            urls.add(link.get('href'))

        return urls

    

# obj = cycle()
# obj.url_cycling()
