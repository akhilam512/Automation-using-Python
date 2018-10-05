#import libraries
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

#firefox driver
browser = webdriver.Firefox()
my_uname = "AM.EN.U4CSE18362"
my_pwd = "amrita1234"

#access AUMS website
browser.get("https://aums-students-am.amrita.edu:8443/cas/login?service=https%3A%2F%2Faums-students-am.amrita.edu%3A8443%2Faums%2FJsp%2FCore_Common%2Findex.jsp")

while(True):

    try:
        logo = browser.find_element_by_xpath("""//*[@id="log_logo"]""") # while the logo is present, keep on logging in
    except:
        break

    uname = browser.find_element_by_id("username")  
    uname.send_keys(my_uname);
    pwd = browser.find_element_by_id("password")
    pwd.send_keys(my_pwd);

    sub = browser.find_element_by_class_name("submit")
    sub.click()
"""

try:  
    library_dropdown = browser.find_element_by_class_name("clTover")
    print("element found for sure")
except:
    print ("ERROR - couldn't find library element - please contact dev")
    
"""
    
"""
# attempt 1  - hover over library element, wait , then find "Renew books" option by id
hover = ActionChains(browser).move_to_element(library_dropdown)
hover.perform()
time.sleep(10)
renew = browser.find_element_by_id("oM_m701")
renew.click()

#failed - nothing happens  ¯\_(._.)_/¯   ¯\_(._.)_/¯
"""
"""
#attempt 2 -using actions, hovering to dropdown and then moving cursor

action = webdriver.comm5on.action_chains.ActionChains(browser)
library_dropdown = browser.find_element_by_class_name("clT")

action.move_to_element_with_offset(library_dropdown,0,30)
action.click()
action.perform()

#failed - nothing happens   ¯\_(._.)_/¯  ¯\_(._.)_/¯  ¯\_(._.)_/¯  ¯\_(._.)_/¯

"""
"""
#attempt 3 - similar to attempt 1, finding library dropdwon by "css selector" instead, then findind "Renew books" by select_by_visible_text method

dropdownID = "#oM_m532"

#dropdownelement = WebDriverWait(browser, 20).until(lambda browser: browser.find_element_by_css_selector(dropdownID)) 
dropdownelement= browser.find_element_by_css_selector("#oM_m532")
dropdownelement.click()

Select(dropdownelement).select_by_visible_text("Renew Books")

#timeout exception , failed (?????)   (ಥ﹏ಥ)

"""
browser.close() # <--- notice 
