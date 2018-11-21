
######    NOTE  #####

'''  Before Running the code make sure selenium is installed and
     The fire fox webdriver is installed into the path '''

               ## By Sayantan



from selenium import webdriver
import time
email="        "    #<-  Enter your email or phone number here between ""
passw="      "    #<-  enter your Password here between ""
driver = webdriver.Chrome(r"C:\Users\sayantan\Downloads\chromedriver.exe")
driver.get("https://facebook.com/")
u_Email=driver.find_element_by_id("email")
u_Email.send_keys(email)
u_Passw=driver.find_element_by_id("pass")
u_Passw.send_keys(passw)
butn=driver.find_element_by_id("loginbutton")
butn.click()
time.sleep(5)
