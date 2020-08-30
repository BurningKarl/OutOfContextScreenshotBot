# coding=utf-8
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

OUTOFCONTEXT_BASE_URL = "https://www.outofcontext.party/lobby/"


def save_outofcontext_screenshot(lobby):
    url = OUTOFCONTEXT_BASE_URL + lobby

    # Set up the browser
    chrome_options = webdriver.chrome.options.Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=chrome_options)

    # Set the username
    driver.get(url)
    time.sleep(1)
    driver.find_element_by_name("playerName").send_keys("ScreenshotBot")
    driver.find_element("xpath", "//button").click()
    time.sleep(1)

    # Take the screenshot
    page_element = driver.find_elements_by_class_name("page")[0]
    driver.set_window_size(page_element.size["width"], page_element.size["height"] + 50)
    menu_element = driver.find_elements_by_class_name("menu")[0]
    filename = driver.title + "_" + datetime.now().isoformat() + ".png"
    menu_element.screenshot(filename)
    driver.quit()

    return filename


if __name__ == "__main__":
    save_outofcontext_screenshot("70q3")
