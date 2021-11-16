#### This program scrapes naukri.com's page and gives our result as a 
#### list of all the job_profiles which are currently present there. 
  
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
  
#url of the page we want to scrape
url = 'https://coinmarketcap.com/currencies/bitcoin/news/'
  
# initiating the webdriver. Parameter includes the path of the webdriver.
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(executable_path=r'C:\Users\HP\Downloads\chromedriver.exe', options = options) 
driver.get(url) 
loadmorebutton = driver.find_element_by_xpath('/html/body/div/div/div/div[2]/div/div[3]/div/div/main/button')
for i in range(4):
    loadmorebutton.click() 
    time.sleep(5) 

  
html = driver.page_source
  
# this renders the JS code and stores all
# of the information in static HTML code.
  
# Now, we could simply apply bs4 to html variable
soup = BeautifulSoup(html, "html.parser")
all_divs = soup.find('div', {'class' : 'wav26n-1 gWmJSZ'})
job_profiles = all_divs.find_all('a')

  
# printing top ten job profiles
count = 0
for job_profile in job_profiles :
    print(job_profile.text)
    print("----------------------------------------------")
    count = count + 1
    if(count == 20) :
        break


  
driver.close() # closing the webdriver