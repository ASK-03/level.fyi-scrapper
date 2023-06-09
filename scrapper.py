import numpy as np
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import argparse
import time

def get_selenium_drivers(url: str='https://google.com') -> object:
    options = Options()
    service=Service('/usr/local/bin/chromedriver')
    options.add_argument("--window-size=1920,1080")
    options.add_experimental_option('detach', True)
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(url)

    print("waiting for the page to load...")
    time.sleep(30)
    print('page loaded...')
    return driver


def get_salary(driver: object) -> list:
    print("clicking some buttons")
    buttons = driver.find_elements(By.XPATH, '//*[@id="blur-prompt_blurPromptCell__qv6Ha"]/div/div/button')
    for button in buttons:
        if "Added Mine Already" in button.get_attribute('innerHTML'):
            button.click()
    
    time.sleep(2)

    buttons = driver.find_elements(By.XPATH, '//*[@id="blur-prompt_blurPromptCell__qv6Ha"]/div/div/button')
    for button in buttons:
        if "Remind Me Later" in button.get_attribute('innerHTML'):
            button.click()

    time.sleep(2)    
    print("fetching the data")

    try:
        page_next_button_div_children = driver.find_element(By.XPATH, '//*[@id="company-page_cardContainerId__MSgxF"]/div/div[1]/div/div[8]/table/tfoot/tr/td/div/div[2]/div').find_elements(By.TAG_NAME, 'button')
    except:
        page_next_button_div_children = driver.find_element(By.CSS_SELECTOR, '#company-page_cardContainerId__MSgxF > div > div.MuiBox-root.css-0 > div > div.MuiTableContainer-root.css-kg5r73 > table > tfoot > tr > td > div > div.MuiGrid-root.MuiGrid-item.css-1iehjkq > div')
    if len(page_next_button_div_children)==1:
        page_limit = 1
    else:
        page_limit = int(page_next_button_div_children[-2].text)

    # logging 
    print(f"number of pages: {page_limit}")

    salaries = []
    for page in range(page_limit):
        print(f"page: {page+1}")
        table = driver.find_element(By.XPATH, '//*[@id="company-page_cardContainerId__MSgxF"]/div/div[1]/div/div[8]/table')
        table = bs(table.get_attribute('innerHTML'), 'lxml')
        element = table.find_all('p', attrs={ 'class': 'MuiTypography-root MuiTypography-body1 css-1voc5jt'})
        time.sleep(1)

        take_next=False
        for idxi, i in enumerate(element):
            if idxi&1==0:
                yoe=i.text[0]
                if yoe=='0':
                    take_next=True 
            if idxi&1==1 and take_next:   
                salaries.append(i.text)
                take_next=False 

    # getting the next page button
        page_next_button_div_children = driver.find_element(By.XPATH, '//*[@id="company-page_cardContainerId__MSgxF"]/div/div[1]/div/div[8]/table/tfoot/tr/td/div/div[2]/div').find_elements(By.TAG_NAME, 'button')
        page_next_button = page_next_button_div_children[-1]
        time.sleep(1)
        if page < page_limit-1:
            print('going to next page ...')
            page_next_button.click()
        else:
            print('last page reached')
        time.sleep(5)

    print("Salaries extracted")

    driver.quit()

    return salaries

def generate_url(company):
    COMPANY = company
    YOE_CHOICE = 'junior'
    YAC_CHOICE = '0'
    MIN_YAC = '0'
    MAX_YAC = '0'
    SINCE_DATE = 'year'  # options - month, year, 2-year, all-time
    OFFSET = '0'  # using 50 offset everytime to make less number of call to the site
    url = f'https://www.levels.fyi/companies/{COMPANY}/salaries/software-engineer?yoeChoice={YOE_CHOICE}&yacChoice={YAC_CHOICE}&minYac={MIN_YAC}&maxYac={MAX_YAC}&sinceDate={SINCE_DATE}&offset={OFFSET}&country=113&limit=50'
    return url

def clean_salaries(salaries: list) -> list:
    print("cleaning it for you...")
    salary_in_int = []
    for idx, salary in enumerate(salaries):
        salaries[idx] = salary.replace('US$', '')
        salaries[idx] = salaries[idx].replace(',', '')
        salary_in_int.append(int(salaries[idx]))
    return salary_in_int

def find_median(salaries: list) -> int:
    print('finding median...')
    salaries = np.array(salaries)
    salaries = salaries.astype(np.int32)
    return np.median(salaries)

def convert_median_to_json(median: int):
    print('converting to json...')
    from json import dumps
    return dumps({'median': median})


def give_output(save):
    if save:
        print('saving to file')
        with open(f'{company}_median_salary.json', 'w') as f:
            f.write(output)
    else:
        print(output)  

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('--company', type=str, default='amazon')
    parser.add_argument('--save', type=bool, default=True)
    args = parser.parse_args()

    company=args.company
    save=args.save

    url = generate_url(company)
    driver = get_selenium_drivers(url)
    salaries=get_salary(driver)
    salaries=clean_salaries(salaries)
    median=find_median(salaries)
    output=convert_median_to_json(median)

    give_output(save)
    
      


