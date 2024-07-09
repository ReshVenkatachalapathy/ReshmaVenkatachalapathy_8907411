# Importing required libraries

# pip install selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.wait import WebDriverWait

# Setting up the webdriver and variables
driver = webdriver.Chrome()

# Navigating to the IMDB homepage and waiting till the page loads
driver.get("https://www.imdb.com/")
driver.maximize_window()
time.sleep(2)
#Set a max wait time
wait = WebDriverWait(driver, 20)
#Set the dynamic wait
element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="home_img"]')))

#Searching for horror movies
search_bar = driver.find_element("xpath", "//*[@id='suggestion-search']")
search_bar.send_keys("Horror Movies")
search_bar.send_keys(Keys.ENTER)
wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[3]/section/div/div[1]/section[1]/h1')))
time.sleep(4)

print("Top Two Horror Movies from IMDB Search List:")
print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")

#Loop to extract details of each movies from search
for i in range(1,3):
    print("Movie: ", i)
    #Select the top 2 movies from the search list
    search_result =driver.find_element("xpath", "//*[@id='__next']/main/div[2]/div[3]/section/div/div[1]/section[2]/div[2]/ul/li["+ str(i) + "]/div[2]")
    search_result.click()

    #Extract the name of the movie
    movie_name = driver.find_element("xpath", "//*[@id='__next']/main/div/section[1]/section/div[3]/section/section/div[2]/div[1]/h1/span")
    print("Movie Name: ", movie_name.text)

    # Extract the ratings of the movie
    rating = driver.find_element("xpath", "//*[@id='__next']/main/div/section[1]/section/div[3]/section/section/div[2]/div[2]/div/div[1]/a/span/div/div[2]/div[1]/span[1]")
    print("Rating: ", rating.text, "/ 10")

    #Click on the cast crew details
    crew_result = driver.find_element("xpath","//*[@id='__next']/main/div/section[1]/section/div[3]/section/section/div[1]/div/div[2]/ul/li/a")
    crew_result.click()
    #Extract the director name
    director_name = driver.find_element("xpath", "//*[@id='fullcredits_content']/table[1]/tbody/tr/td[1]/a")
    print("Director Name: ",director_name.text)
    print("About Director:")

    #Extract the director details
    director_page = driver.find_element("xpath","//*[@id='fullcredits_content']/table[1]/tbody/tr/td[1]/a")
    director_page.click()
    time.sleep(3)
    director_movies = driver.find_element("xpath","//*[@id='__next']/main/div/section[1]/section/div[3]/section/section/div[3]/div/div[1]/section/div/div/div/div")
    print(director_movies.get_attribute("innerText"))

    driver.back()
    time.sleep(3)
    driver.back()
    time.sleep(3)
    driver.back()
    time.sleep(3)
    print("===============================================================================================================================================================================================")

