
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import pandas as pd

def driver_init():
    fop = Options()
    fop.add_argument('--headless')
    fop.add_argument('--window_size1920x1080')
    return webdriver.Firefox(options = fop)

def scrape_iris(driver):
    flowers = ['setosa', 'versicolor', 'virginica']
    driver.get('https://gist.github.com/curran/a08a1080b88344b0c8a7')
    dataframe = {'sepal_length' : [], 'sepal_width' : [], 'petal_length' : [],  \
                 'petal_width' : [], 'species' : []}
    data = driver.find_elements_by_tag_name('td')
    lists = [d for d in dataframe.keys() if d != 'species']
    num = 0
    for d in data:
        if num == 4:
            num = 0
        d = d.get_attribute('innerHTML')
        if d in flowers:
            dataframe['species'].append(d)
        try:
            check = str(float(d))
            dataframe[lists[num]].append(float(d))
            num += 1
        except:
            pass
    return pd.DataFrame(dataframe)
    driver.quit()
