# coding=utf-8
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import (
    NoSuchElementException as PageDesignChangedException,
)

OUTOFCONTEXT_BASE_URL = "https://www.outofcontext.party/lobby/"


class InvalidLobbyException(Exception):
    pass


class PageNotFoundException(Exception):
    pass


def save_outofcontext_screenshot(lobby):
    url = OUTOFCONTEXT_BASE_URL + lobby

    # Set up the browser
    chrome_options = webdriver.chrome.options.Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=chrome_options)

    # Load the webpage
    driver.get(url)
    time.sleep(3)

    # Check the validity of the lobby id
    title_div = driver.find_element_by_class_name("title")
    if title_div.text == "Invalid Lobby":
        raise InvalidLobbyException(f"The lobby id {lobby!r} is invalid.")
    elif title_div.text == "Page Not Found":
        raise PageNotFoundException(f"The url {url!r} was not found.")

    # Set the username
    driver.find_element_by_name("playerName").send_keys("ScreenshotBot")
    driver.find_element("xpath", "//button").click()
    time.sleep(1)

    # Resize the browser window
    page_element = driver.find_element_by_class_name("page")
    driver.set_window_size(page_element.size["width"], page_element.size["height"] + 50)

    # Take the screenshot
    menu_element = driver.find_elements_by_class_name("menu")[0]
    filename = driver.title + "_" + datetime.now().isoformat() + ".png"
    menu_element.screenshot(filename)
    driver.quit()

    return filename


if __name__ == "__main__":
    save_outofcontext_screenshot("70q3")
