from selenium import webdriver #for automating web browsers. It allows you to control the browser, navigate to URLs, 
                               #find elements on a page, and perform various actions.
from selenium.webdriver.chrome.service import Service #It helps in launching the browser with the appropriate configurations.
from selenium.common.exceptions import NoSuchElementException #t is raised when an element cannot be found on the page or does not exist in the DOM
from selenium.webdriver.common.keys import Keys #provides various keyboard keys that can be sent to web elements, such as Enter, Tab, Shift, etc.
from selenium.webdriver.support.ui import WebDriverWait # It provides a mechanism for waiting until certain conditions are met before proceeding with the script execution
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.by import By
from userinfo import username, password
import time

class Github:
    chrome_driver_path = "C:\\Users\\umutcan\\Downloads\\chromedriver-win64\\chromedriver" 

    def __init__(self) -> None:
        
        service = Service(Github.chrome_driver_path)
        self.browser = webdriver.Chrome(service=service)
        self.baseUrl = "https://github.com/"    
        self.username = username
        self.password = password
         
    def timeSleep(self): 
        time.sleep(5)  # 5 second cooldown
        
        # Loop waiting for an input from the keyboard
        input("Tarayiciyi kapatmak icin Enter tuşuna basin...")
        self.browser.quit()
    
    def signIn(self):
        self.browser.get(self.baseUrl + "login")
        usernameInput = self.browser.find_element("name","login")
        passwordInput = self.browser.find_element("name","password")
        btn = self.browser.find_element("name","commit")
        
        usernameInput.send_keys(self.username)
        passwordInput.send_keys(self.password)
        btn.click()  
  
        self.timeSleep()
        
    def findRepositories(self,keyword):
        self.browser.get(self.baseUrl)
        wait = WebDriverWait(self.browser, 10)
        searchInput = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[name="query-builder-test"]')))
        searchInput = self.browser.find_element("name","query-builder-test") 
        
       
        searchInput.send_keys(keyword)
        searchInput.send_keys(Keys.ENTER) 
        
        print(self.browser.page_source)
        
        self.timeSleep()
        
    def getfollowers(self):
        self.browser.get(self.baseUrl + self.username + "?tab=followers")
        
        items = self.browser.find_elements(By.CSS_SELECTOR,".d-table.table-fixed")
        
        print(f"------FOLLOWERS----------\n")
        for item in items:
            name = item.find_elements(By.TAG_NAME,"div")[1].find_elements(By.TAG_NAME,"span")[0].text
            username = item.find_elements(By.TAG_NAME,"div")[1].find_elements(By.TAG_NAME,"span")[1].text
            print(f"name: {name} username: {username} \n")            
            
        self.timeSleep()
        
    def getFollowing(self):
        self.browser.get(self.baseUrl + self.username + "?tab=following")
        
        items= self.browser.find_elements(By.CSS_SELECTOR,".d-table.table-fixed")

        print(f"------FOLLOWING----------\n")
        for item in items:
            name = item.find_elements(By.TAG_NAME,"div")[1].find_elements(By.TAG_NAME,"span")[0].text
            username = item.find_elements(By.TAG_NAME,"div")[1].find_elements(By.TAG_NAME,"span")[1].text
            print(f"name: {name} username: {username} \n")            
            
        self.timeSleep()
        
while(True):
    app = Github()
    choose = input("sign in:1\nget Repositories:2\nget Followers:3\nget Following:4\nExit:5\nChoose: ")
    if choose == "1":
        app.signIn()
        
    elif choose == "2":
        key = input("type the word you want to search: ")
        app.findRepositories(key)
        
    elif choose == "3":
        app.getfollowers()
        
    elif choose == "4":
        app.getFollowing()
        
    elif choose == "5":
        break
    
    else:
        print("Invalid value")