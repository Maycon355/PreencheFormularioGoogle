import time
from selenium import webdriver
from selenium.webdriver.chrome import options
from selenium.webdriver.chrome.options import Options
import os
from time import sleep

i = 1
count = 1

while i < 6:
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")
    url = "https://docs.google.com/forms/d/e/1FAIpQLSeYvId2KmlVLzW2ccQz5SHkZ6mq2lzfpzm0Z9ZDHS2oNkwvsQ/viewform?fbzx=4516857556575108506"
    driver = webdriver.Chrome(chrome_options=options)
    driver.get(url)

    sleep(1)
    # login
    driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div[1]/div[2]/div[1]/div/div[1]/input').send_keys("luan.filipin@gttech.com.br")  # email
    driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys("Luan Brito Filipin")  # nome
    driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys("Tecnologia da Informação| MATRIZ")  # setor
    driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span').click()  # setor

    ######## ENTROU NO QUESTIONÁRIO ############
    # 1
    driver.find_element_by_id('i9').click()
    # 2
    driver.find_element_by_id('i25').click()
    # 3
    driver.find_element_by_id('i38').click()
    # 4
    driver.find_element_by_id('i54').click()
    # 5
    driver.find_element_by_id('i64').click()
    # 6
    driver.find_element_by_id('i80').click()
    # 7
    driver.find_element_by_id('i87').click()
    # 8
    driver.find_element_by_id('i103').click()
    # 9
    driver.find_element_by_id('i119').click()

    # //*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]/span/span
    driver.find_element_by_xpath(
        '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div[2]/span/span').click()

    print(count)
    count += 1
    driver.quit()
