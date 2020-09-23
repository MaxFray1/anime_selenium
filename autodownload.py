import os.path
import re
import time
import csv
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


def download_anime(driver, anime):
    driver.get(anime[0])
    time.sleep(1)
    try:
        for i in range(int(anime[1]), int(anime[2])):
            episode = driver.find_element_by_id('p'+str(i))
            actions = ActionChains(driver)
            actions.move_to_element(episode)
            actions.click(episode)
            actions.perform()
            time.sleep(1) 
            driver.switch_to.frame(driver.find_element_by_tag_name('iframe'))
            downlink = driver.find_element_by_link_text('720p (HD)').get_attribute('href')
            driver.get(downlink)
            name = re.findall(r'\W720\W\d*.mp4', downlink)[0].replace('/','_') +'.crdownload'
            print(name)
            time.sleep(5)
            print(os.path.exists('/home/xhazker/Downloads/'+name))
            while(True):
                if not os.path.exists('/home/xhazker/Downloads/'+name):
                    break
                time.sleep(1)
            driver.switch_to.default_content()
            print('WELL DONE!Next!')
    finally:
        driver.quit()


if __name__ == ('__main__'):
    PATH = '/home/xhazker/Programs/chromedriver_linux64/chromedriver'
    driver = webdriver.Chrome(PATH)
    with open('anime.csv', newline='') as csvfile:
        anime = list(csv.reader(csvfile, delimiter=';'))
    download_anime(driver, anime[0])

