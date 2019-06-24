from pyvirtualdisplay import Display
from selenium import webdriver

display = Display(visible=0, size=(800, 600))
display.start()

driver = webdriver.Chrome('./chromedriver')
driver.get('https://www.premierleague.com/tables?co=1&se=42&mw=-1&ha=-1')
print(driver.title)
