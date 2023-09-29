from flask import Flask , request , render_template
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

app = Flask(__name__)


def browser_setup(browse_visually = "no"):
    """ブラウザを起動する関数"""
    #ブラウザの設定
    options = webdriver.ChromeOptions()
    if browse_visually == "no":
        options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    #ブラウザの起動
    browser = webdriver.Chrome(options=options , service=ChromeService(ChromeDriverManager().install()))
    browser.implicitly_wait(3)
    return browser


@app.route("/" , methods=['GET', 'POST'])
def index():
    if request.method == 'POST' and request.form['start_scraping'] == "true":
        browse_visually = request.form['browse_visually'] 

        searched_url = "https://www.bookoffonline.co.jp/"
        driver = browser_setup(browse_visually)
        driver.get(searched_url)
        p_text = driver.find_element(By.TAG_NAME , "p").text

        return render_template("index.html" , p_text = p_text)

    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
