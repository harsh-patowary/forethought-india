
import requests
from flask import Flask, send_file, render_template, request, url_for, flash, redirect
from bs4 import BeautifulSoup
import cycler
import extractor

app = Flask(__name__)
cycler_obj = cycler.cycle()
extractor_obj = extractor.extract()


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        link = request.form.get('url')
        print(link)
        index_urls = set()
        index_urls = cycler_obj.url_cycling(link)
        emails = []
        for url in index_urls:
        
            emails = extractor_obj.email_extracting(url)
            extractor_obj.write_file(emails, url)
            if(len(emails)>0):
                # print(emails)
                print("**Crawl Successfull**")
                
                

            else:
                print(f"+Empty Link+ {url}+")
                print(f"Empty links are links with null extracts")
        
        return render_template('index.html')

    return render_template('index.html')

@app.route('/download', methods=['GET', 'POST'])
def download_file():
	#path = "html2pdf.pdf"
	#path = "info.xlsx"
	#path = "simple.docx"
	path = "data/emails.csv"
	return send_file(path, as_attachment=True)
    
