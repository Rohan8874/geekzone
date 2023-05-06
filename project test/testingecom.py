import random
import time
from pyhtmlreport import Report
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
report = Report()
driver: WebDriver = webdriver.Chrome(executable_path="C:\Program Files (x86)")
report.setup(
report_folder=r'Reports',
module_name='Device',
release_name='Test V1',
selenium_driver=driver
)
driver.get('http://127.0.0.1:8000/')
# Test Case 1
try:
report.write_step(
'Go to Landing Page',
status=report.status.Start,
test_number=1
)
assert (driver.title == 'geekzone')
report.write_step(
'Landing Page loaded Successfully.',
status=report.status.Pass,
screenshot=True
)
except AssertionError:
report.write_step(

'Landing Page loaded Successfully.',
status=report.status.Fail,
screenshot=True
)
except Exception as e:
report.write_step(
'Something went wrong!</br>{e}',
status=report.status.Warn,
screenshot=True
)

# Test Case 2
try:
report.write_step(
'Registration',
status=report.status.Start,
test_number=2
)

driver.find_element(By.XPATH, '//*[@id="id_username"]').click()
time.sleep(1)
driver.find_element(By.NAME, 'username').send_keys('geek')
driver.find_element(By.ID, 'password').send_keys('geek@#123')
driver.find_element(By.ID, 'password').send_keys('geek@1234')
driver.find_element(By.NAME, 'email').send_keys('geek@gmail.com')


time.sleep(1)
driver.find_element(By.XPATH, '/html/body/main/div/div/div/form/input[6]').click()
assert (driver.title == 'Register in  - geekzone')
report.write_step(
'Successfully Rgister ',
status=report.status.Pass,
screenshot=True

)
except AssertionError:
report.write_step(
'Failed to Register',
status=report.status.Fail,
screenshot=True
)
except Exception as e:
report.write_step(
'Something went wrong!</br>{e}',
status=report.status.Warn,
screenshot=True
)

# Test Case 3
try:
report.write_step(
'Login for a user',
status=report.status.Start,
test_number=3
)
driver.find_element(By.NAME,'username').send_keys('geek')
time.sleep(1)
driver.find_element(By.ID, 'password').send_keys('geek@#123')
time.sleep(1)
driver.find_element(By.XPATH, '/html/body/main/div/div/div/form/input[4]').click()
assert (driver.title == ' User - Profile')
report.write_step(
'Successfully login ',
status=report.status.Pass,
screenshot=True
)
except AssertionError:
report.write_step(
'Failed to login',
status=report.status.Fail,
screenshot=True
)
except Exception as e:
report.write_step(
'Something went wrong!</br>{e}',
status=report.status.Warn,

screenshot=True
)

# Test Case 4
try:
report.write_step(
'Information of  user',
status=report.status.Start,
test_number=4
)
driver.find_element(By.NAME,'Name').send_keys('Geekzone')
time.sleep(1)
driver.find_element(By.NAME, 'Locality').send_keys('Dhaka')
time.sleep(1)
driver.find_element(By.NAME, 'City').send_keys('Dhaka')
time.sleep(1)
driver.find_element(By.NAME, 'Mobile').send_keys('01478963214')
time.sleep(1)
driver.find_element(By.NAME, 'State').send_keys('Dhaka')
time.sleep(1)
driver.find_element(By.NAME, 'Zip_Code').send_keys('1234')
time.sleep(1)
driver.find_element(By.XPATH, '/html/body/main/div/div/div/form/input[4]').click()
assert (driver.title == ' User - Profile')
report.write_step(
'Successfully Update ',
status=report.status.Pass,
screenshot=True
)
except AssertionError:
report.write_step(
'Failed to Update',
status=report.status.Fail,
screenshot=True
)
except Exception as e:
report.write_step(
'Something went wrong!</br>{e}',
status=report.status.Warn,

screenshot=True
)

# Test Case 5
try:
report.write_step(
'Back to Landing Page',
status=report.status.Start,
test_number=5
)
driver.find_element(By.XPATH, '/html/body/nav/div/div/ul/li[1]/a').click()
assert (driver.title == 'Landing')
report.write_step(
'Back to Landing Page',
status=report.status.Pass,
screenshot=True

)
except AssertionError:
report.write_step(
'Failed',
status=report.status.Fail,
screenshot=True
)
except Exception as e:
report.write_step(
'Something went wrong!</br>{e}',
status=report.status.Warn,
screenshot=True
)

# Test Case 6
try:
report.write_step(
'Goto to Password Change Page',
status=report.status.Start,
test_number=6
)
driver.find_element(By.XPATH, '/html/body/nav/div/ul/li[1]/ul/li[3]/a').click()
assert (driver.title == 'Change Password - Geekzone')
report.write_step(
'Change Password Page Loaded',
status=report.status.Pass,
screenshot=True
)
except AssertionError:
report.write_step(
'Failed to Load Change password page',
status=report.status.Fail,
screenshot=True
)
except Exception as e:
report.write_step(
'Something went wrong!</br>{e}',
status=report.status.Warn,
screenshot=True
)

# Test Case 7
try:
report.write_step(
'Password Change',
status=report.status.Start,
test_number=7
)
driver.find_element(By.NAME, 'old_password').send_keys('geek@1234')
time.sleep(1)
driver.find_element(By.NAME, 'new_password').send_keys('zone@#123')
time.sleep(1)
driver.find_element(By.NAME, 'new_password').send_keys('zone@#123')
time.sleep(1)
driver.find_element(By.XPATH, '/html/body/main/div/div/div[2]/form/button').click()
time.sleep(1)
assert (driver.title == 'Sign in')
report.write_step(
'Password Changed',
status=report.status.Pass,
screenshot=True
)
except AssertionError:
report.write_step(
'Failed to Password Change',
status=report.status.Fail,
screenshot=True
)
except Exception as e:
report.write_step(
'Something went wrong!</br>{e}',
status=report.status.Warn,
screenshot=True
)

# Test Case 8
try:
report.write_step(
'Go to Product Page',

status=report.status.Start,
test_number=8
)
driver.find_element(By.XPATH, '/html/body/nav/div/div/ul/li[2]/a').click()
time.sleep(2)
driver.find_element(By.XPATH, '/html/body/nav/div/div/ul/li[2]/ul/li[1]/a').click()
time.sleep(1)
assert (driver.title == 'Smart Phones')
report.write_step(
'User Select Phones',
status=report.status.Pass,
screenshot=True
)
except AssertionError:
report.write_step(
'Failed to select',
status=report.status.Fail,
screenshot=True
)
except Exception as e:
report.write_step(
'Something went wrong!</br>{e}',
status=report.status.Warn,
screenshot=True
)

# Test Case 9
try:
report.write_step(
'Go to Cart Page',

status=report.status.Start,
test_number=9
)
driver.find_element(By.XPATH, '/html/body/main/div/div/div[2]/div/div[1]/a/div/img').click()
time.sleep(2)
driver.find_element(By.XPATH, '/html/body/main/div/div/div[2]/form/button').click()
time.sleep(1)
assert (driver.title == 'Add to Cart')
report.write_step(
'Items in Cart',
status=report.status.Pass,
screenshot=True
)
except AssertionError:
report.write_step(
'Failed to cart',
status=report.status.Fail,
screenshot=True
)
except Exception as e:
report.write_step(
'Something went wrong!</br>{e}',
status=report.status.Warn,
screenshot=True
)

# Test Case 10
try:
report.write_step(
'Logout User',

status=report.status.Start,
test_number=10
)
driver.find_element(By.XPATH, '').click()
time.sleep(2)
driver.find_element(By.XPATH, '').click()
time.sleep(1)
assert (driver.title == '')
report.write_step(
'User has been logged out.',
status=report.status.Pass,
screenshot=True
)
except AssertionError:
report.write_step(
'Failed to Logout',
status=report.status.Fail,
screenshot=True
)
except Exception as e:
report.write_step(
'Something went wrong!</br>{e}',
status=report.status.Warn,
screenshot=True
)

)
finally:
report.generate_report()
driver.quit()
