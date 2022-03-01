from flask import Flask, render_template, request, redirect

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import shutil
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

app = Flask(__name__)
# defining a route
@app.route("/", methods=['GET']) # decorator
def home(): # route handler function
    # returning a html template
    return render_template('index.html')

@app.route('/download',methods=['POST', "GET"])
def download():

    if request.method=='POST':
        result = request.form

        imglink = result['link']
        flnm = result['flnm']
        option = result['options']

        link = imglink
        filename = flnm

        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

        By.CLASS_NAME
        def downloadImage(url, filename):
            driver.get(url)
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "FFVAD"))
            )
            s = element.get_attribute('src')
            r = requests.get(s, stream=True)

            with open(filename, 'wb') as f:
                shutil.copyfileobj(r.raw, f)

        def downloadVideo(url, filename):
            driver.get(url)
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "tWeCl"))
            )
            s = element.get_attribute('src')
            r = requests.get(s, stream=True)

            with open(filename, 'wb') as f:
                for chunk in r.iter_content(chunk_size=1024*1024):
                    if chunk:
                        f.write(chunk)
        
        if option == "video":
            downloadVideo(link, filename+".mp4")
        elif option == "image":
            downloadImage(link, filename+".png")


        driver.close()

    return redirect("/")

app.run(debug = True) 