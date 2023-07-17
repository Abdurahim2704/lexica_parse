from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from functions import save_images, parseLexica
from flask import Flask


app = Flask(__name__)


@app.get("/image/<description>/<index>")
def get_prompt(description, index):
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    elements = parseLexica(description, driver)
    srcs = save_images(elements)
    url = srcs[int(index)]
    driver.quit()
    return url


app.run();
