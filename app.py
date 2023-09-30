import streamlit as st
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService


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



def main():
    st.title("Render.com の selenium 実証")
    st.write("<p></p>", unsafe_allow_html=True)

    searched_url = "https://shopping.bookoff.co.jp/"
    print(f"ドライバーセット完了")

    if st.button("スクレイピング開始"):
        st.write("<p><br></p>", unsafe_allow_html=True)

        driver = browser_setup()
        driver.get(searched_url)
        print(f"ページアクセス完了")
        driver.implicitly_wait(5)
        
        week_recommend_elements = driver.find_element(By.CSS_SELECTOR , "section.recommend__inner").find_elements(By.CSS_SELECTOR , "div.recommend__list")
        print(f"該当のhtml要素取得完了")
        week_recommend_list = []
        st.write(f"<h3>正常に取得できました</h3>" , unsafe_allow_html=True)
        for element in week_recommend_elements:
            week_recommend_text = element.text
            st.write(week_recommend_text)

if __name__ == '__main__':
    main()


