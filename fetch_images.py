from selenium import webdriver
from time import sleep
import urllib
import requests
import random
import os
import shutil

url = "https://www.indiaglitz.com/aamir-khan-photos-hindi-actor-2628990-7950"
image_directory_name = "aamir_khan_images"


def fetch_images(url,image_directory_name):
    """Function to Retrive and save images from the given URL"""
    try:
        driver = webdriver.Firefox()
        driver.get(url)
        driver.find_element_by_xpath("/html/body/div[7]/div[5]/div/div[2]/a[1]")\
                .click()
        sleep(1)
        last_height = driver.execute_script("return document.body.scrollHeight")
        SCROLL_PAUSE_TIME = 3
        while True:
            
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            sleep(SCROLL_PAUSE_TIME)
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height


        links = driver.find_elements_by_xpath('//img[@class="galleryimage gallery-items"]')
        
        image_directory_path = os.path.join(os.getcwd(),image_directory_name)
        
        if os.path.exists(image_directory_path):
            shutil.rmtree(image_directory_path)
        
        os.mkdir(image_directory_path)
        os.chdir(image_directory_path)

        for link_index in range(len(links)):    
            src = links[link_index].get_attribute('src')
            full_name = str(link_index) + '.jpg'
            urllib.request.urlretrieve(src, full_name)
            print(full_name)
    except Exception as e:
        print(e)

if __name__=="__main__":
    fetch_images(url,image_directory_name)

