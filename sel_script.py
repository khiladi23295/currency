from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def scrape_data():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_experimental_option(
        "prefs", {
            # block image loading
            "profile.managed_default_content_settings.images": 2,
        }
    )

    driver = webdriver.Chrome(options=options)
    url = "https://www.livecharts.co.uk/currency-strength.php"
    driver.get(url)
    subElements = driver.find_elements(By.XPATH, "//*[@id='rate-outercontainer']/div")

    # Your scraping logic here
    strengthCount = 0
    strengthDict = {}
    for i in subElements:
        if (i.get_attribute("style") != "background-image: none;" and i.get_attribute(
                "id") != "map-innercontainer-symbol"):
            strengthCount += 1
        if (i.get_attribute("id") == "map-innercontainer-symbol"):
            strengthDict[i.text] = strengthCount
            strengthCount = 0
    driver.close()
    return strengthDict
