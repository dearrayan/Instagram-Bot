from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class InstaBot:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()

    def login(self):
        bot = self.bot
        bot.get('https://www.instagram.com/')
        time.sleep(3)
        email = bot.find_element_by_name('username')
        password = bot.find_element_by_name('password')
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(4)

    def like_post(self, hashtag):
        bot = self.bot
        bot.get('https://www.instagram.com/explore/tags/'+hashtag+'/')
        time.sleep(3)
        bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        time.sleep(3)
        elems = bot.find_elements_by_xpath("//a[contains(@href, '/p/')]")
        links = [elem.get_attribute('href') for elem in elems]

        try:
            for link in links:
                bot.get(link)
                bot.find_element_by_tag_name("svg").click()
                time.sleep(8)
        except Exception as ex:
            print("Waiting")
            time.sleep(60)

ed = InstaBot('your_username', 'your_password')
ed.login()
ed.like_post('poems')