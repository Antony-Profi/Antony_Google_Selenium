import threading
import pyglet
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def google():
    driver = webdriver.Chrome()
    driver.get('http://www.google.com/')
    time.sleep(5)
    search_box = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
    search_box.send_keys('ChromeDriver')
    search_box.submit()
    time.sleep(5)
    driver.quit()


def music():
    sound = pyglet.media.load(r'C:\1.mp3', streaming=False)
    sound.play()
    pyglet.app.run()


t1 = threading.Thread(target=music)
t2 = threading.Thread(target=google)
t1.start()
t2.start()
t1.join()
t2.join()
