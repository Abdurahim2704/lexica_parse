from requests import get
from selenium.webdriver.common.by import By


def save_images(elements):
    url_list = []
    for i in elements:
        url_list.append(i)
        if len(url_list) == 5:
            break
    return url_list


def parseLexica(prompt, driver):
    query = "+".join(prompt.split(" "))
    url = f"https://lexica.art/?q={query}"
    driver.get(url)
    elements = driver.find_elements(By.XPATH, "//div[@role='gridcell']/a/img", )
    elements = map(lambda x: x.get_attribute("src"), elements)
    return elements
