import importlib
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import re
import pandas as pd
import os
import requests
from lxml import html
import config


def spotifyLogIn():
    spotifyInfo = {
        "username": config.username,
        "password": config.password,
        "recaptcha-token": config.recaptchaToken
    }

    sessionReq = requests.session()
    loginPage = 'https://accounts.spotify.com/en/login?continue=https:%2F%2Fopen.spotify.com%2Fbrowse%2Ffeatured'
    login = sessionReq.get(loginPage)
    tree = html.fromstring(login.text)
    authenToken = list(set(tree.xpath("//input[@id='recaptcha-token']/@value")))

    login = sessionReq.post(
        loginPage,
        data = spotifyInfo,
        headers = dict(referer=loginPage)
    )
    return 0
def scrapeCities():
    drakeURL = 'https://open.spotify.com/artist/3TVXtAsR1Inumwj472S9r4/about'
    
    
    # create a new Firefox session
    driver = webdriver.Firefox()
    driver.implicitly_wait(30)
    driver.get(drakeURL)

    python_button = driver.find_element_by_class_name('ArtistAbout__city__name') 
    # python_button.click()
    
    pageData = requests.get(drakeURL, timeout = 5)
    scraper = BeautifulSoup(pageData.content, 'html.parser')# (driver.page_source, 'lxml') #
    # print(scraper.prettify)
    mainText = scraper.find_all('script')[5]
    # print(mainText)
    mainTextString = str(mainText)
    cities = mainTextString.split("cities", 1)[1] 
    print(cities)
    driver.close()
def main():
        # spotifyLogIn()
        scrapeCities()

if __name__ == '__main__':
    main()