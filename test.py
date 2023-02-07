import pandas as pd
import csv
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options

# Setting a base url for where to find all the designers on grailed
base_url = "https://www.grailed.com/designers/"
# open up chrome
chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome('data/chromedriver',options=chrome_options) # replace webdrive location with ones own
driver.get(base_url)
# wait 30 sec will quit if takes over 30 seconds
#timeout =
try:
    WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.XPATH, "//div[@id='app']")))
except TimeoutException:
    print("Timed out")
    driver.quit()
    
# gathering all links on designer page
results = driver.find_elements_by_xpath("//a[@href]")
# Making a list of all the links 
Link =[]
for result in results:
        link = result.get_attribute("href") # grabbing the link attribute
        Link.append(link)
      
# Turn the Links into a DataFrame
ItemDF=pd.DataFrame(Link,columns=['Link'])

# filtering out links that are not designer page links
ItemDF = ItemDF[ItemDF['Link'].str.contains("designers/")]