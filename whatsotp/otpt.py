from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from urllib.parse import quote
import time


# Config
login_time = 30     # Time for login (in seconds)
new_msg_time = 5    # TTime for a new message (in seconds)
send_msg_time = 5   # Time for sending a message (in seconds)
country_code = 91   # Set your country code

# Create driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Encode Message Text
otp_token = 6194
msg = f'Your OTP for login is: {otp_token}'
num = '7798586194'
# Open browser with default link



link = 'https://web.whatsapp.com'
driver.get(link)
time.sleep(login_time)
link = f'https://web.whatsapp.com/send/?phone={country_code}{num}&text={msg}'
driver.get(link)
time.sleep(new_msg_time)
actions = ActionChains(driver)
actions.send_keys(Keys.ENTER)
actions.perform()
time.sleep(send_msg_time)

#driver.quit()




