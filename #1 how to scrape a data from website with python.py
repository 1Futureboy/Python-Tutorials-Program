#import modules
import bs4                          
from selenium import webdriver


#create driver
driver=webdriver.PhantomJS(executable_path=r"C:\Users\Aadarsh Raj\Downloads\Programs\phantomjs-2.1.1-windows\bin\phantomjs.exe")

#Url Of The Website You Want To Scrape A Data
url="http://hackglaxy.blogspot.com/"


#downlaod page_source
driver.get(url)
print(driver.page_source)  

