from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

PROMISED_DOWN = 150
PROMISED_UP = 10
CHROME_DRIVER_PATH = your chromedriver path
TWITTER_EMAIL = your twitter email
TWITTER_PASSWORD = your twitter password
MY_OPERATOR = your operator name


class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        self.down = 0
        self.up = 0
        self.opt = Options()
        self.opt.headless = True
        self.chrome_driver_path = CHROME_DRIVER_PATH
        self.ser = Service(self.chrome_driver_path)
        self.driver = webdriver.Chrome(service=self.ser)

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")

        go_button = self.driver.find_element(By.CSS_SELECTOR, ".start-button a")
        go_button.click()

        time.sleep(60)
        self.down = self.driver.find_element(By.XPATH,
                                             '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div['
                                             '3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        self.up = self.driver.find_element(By.XPATH,
                                           '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div['
                                           '3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        self.driver.quit()

        self.driver1 = webdriver.Chrome(service=self.ser)

    def tweet_at_provider(self):
        self.driver1.get('https://twitter.com/i/flow/login')
        time.sleep(2)
        self.email = self.driver1.find_element(By.XPATH, '//input[@autocomplete="username"]')
        self.email.send_keys(TWITTER_EMAIL)
        self.email.send_keys(Keys.TAB)
        self.email.send_keys(Keys.ENTER)
        time.sleep(2)
        self.pas = self.driver1.find_element(By.NAME, 'password')
        self.pas.send_keys(TWITTER_PASSWORD)
        self.pas.send_keys(Keys.TAB + Keys.TAB + Keys.TAB + Keys.ENTER)
        time.sleep(2)
        self.tweet=self.driver1.find_element(By.XPATH,"//div[contains(@aria-label, 'Tweet text')]")
        self.tweet.send_keys(
            f'Hey{MY_OPERATOR}.My down speed is {self.down} and up is {self.up} instead of {PROMISED_DOWN}down & {PROMISED_UP}up')
        self.button = self.driver1.find_element(By.XPATH, '//div[@data-testid="tweetButtonInline"]').click()
        time.sleep(10)
        self.driver1.quit()


bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
bot.get_internet_speed()
bot.tweet_at_provider()
