import time
from selenium import webdriver
import logging
import os
import shutil
from datetime import datetime, timedelta

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs", prefs)
chrome_options.add_argument("start-maximized")
LOG_FILENAME = 'Facebook.log'
logging.basicConfig(filename=LOG_FILENAME,
                    level=logging.INFO,
                    format='%(asctime)s %(levelname)s %(message)s',
                    filemode='w')

driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=r'Chrome Driver Location')  # Optional argument, if not specified will search path.
driver.get('YoupageURL/insights')


try:
    email = driver.find_element_by_id("email")
    email.send_keys('Your User Name')
    password = driver.find_element_by_id("pass")
    password.send_keys('Your Password')
    loginButton = driver.find_element_by_id("loginbutton")
    loginButton.click()
    time.sleep(2)
    logging.info(':Logged Into Facebook Page Analytics')
except:
    logging.info(':Failed to Login Facebook Page Analytics')
    

try:
    driver.find_element_by_xpath("//a[@class='_58dq _55pi _2agf _4o_4 _4jy0 _4jy3 _517h _51sy _42ft']").click()
    driver.find_element_by_xpath("//span[text()='Yesterday']").click()
    driver.find_element_by_xpath("//div[. = 'Export Data']").click()
    time.sleep(3)
    driver.find_element_by_xpath("//button[@data-testid='export_button']").click()
    logging.info(':Export Initiated')
except:
    logging.info(':Export Initiation Failed')



try:    
    before = os.listdir('Download Folder Location')
    time.sleep(8)   
    driver.find_element_by_xpath("//div[. = 'Export Data']").click()
    time.sleep(2)
    after = os.listdir('Download Folder Location')
    logging.info(':Downloading Page Analytics File')
    change = set(after) - set(before)
    print (change)
    if len(change) == 1:
        file_name = change.pop()
        src_dir="Download Folder Location"
        src_file = os.path.join(src_dir, file_name)
        dst_dir="Destination directory of Analytics File"
        shutil.copy(src_file,dst_dir)
        dst_file = os.path.join(dst_dir, file_name)
        fn=datetime.strftime(datetime.now() - timedelta(1), '%Y%m%d')
        fn=str(fn)+str("-Facebook.xls")
        new_dst_file_name = os.path.join(dst_dir, fn)
        os.rename(dst_file, new_dst_file_name)
        #print(file_name)
        logging.info(':Downloaded Page Analytics File is '+str(file_name))
    else:
        print ("More than one file or no file downloaded")

except:
    logging.info(':Downloading Page Analytics File Failed')

try:
    before = os.listdir('Download Folder Location')
    driver.find_element_by_xpath("//input[@value='post_level'][@class='uiInputLabelInput uiInputLabelRadio']").click()
    driver.find_element_by_xpath("//button[@data-testid='export_button']").click()
    time.sleep(8)
    after = os.listdir('Download Folder Location')
    logging.info(':Downloading Posts Analytics File')
    change = set(after) - set(before)
    print (change)
    if len(change) == 1:
        file_name = change.pop()
        src_dir="Download Folder Location"
        src_file = os.path.join(src_dir, file_name)
        dst_dir="Destination directory of Analytics File"
        shutil.copy(src_file,dst_dir)
        dst_file = os.path.join(dst_dir, file_name)
        fn=datetime.strftime(datetime.now() - timedelta(1), '%Y%m%d')
        fn=str(fn)+str("-FacebookPosts.xls")
        new_dst_file_name = os.path.join(dst_dir, fn)
        os.rename(dst_file, new_dst_file_name)
        #print(file_name)
        logging.info(':Downloaded Posts Analytics File is '+str(file_name))
    else:
        print ("More than one file or no file downloaded")

except:
    logging.info(':Downloading Posts Analytics File Failed')
logging.shutdown()
driver.close()
