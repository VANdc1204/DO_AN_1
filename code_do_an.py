from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
import os
import wget
import getpass

facebook_username = input("Your Facebook username: ")
facebook_password = getpass.getpass("Your Facebook password: ")
facebook_user_profile_url = input("facebook_user_profile_url: ")

driver = webdriver.Chrome(executable_path="Chromedriver.exe")
driver.get("http://facebook.com")

txtUser=driver.find_element_by_id("email")
txtUser.send_keys(facebook_username)

txtPass=driver.find_element_by_id("pass")
txtPass.send_keys(facebook_password)   

txtPass.send_keys(Keys.ENTER)
time.sleep(5)


time.sleep(5)
images = [] 

driver.get(facebook_user_profile_url+"/photos_by")
time.sleep(5)
    
    #Cuộn xuống trang
    #Cuộn xuống (0,10) thì sẽ tải được 650+ ảnh
for j in range(0,1):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(10)

    #Tìm tất cả các element có tag name là a
anchors = driver.find_elements_by_tag_name('a')
anchors = [a.get_attribute('href') for a in anchors]
    #down xuống link của các element
anchors = [a for a in anchors if str(a).startswith("https://www.facebook.com/photo")]
    
print('Found ' + str(len(anchors)) + ' links to images')
    
for a in anchors:
    driver.get(a) 
    time.sleep(5) 
    img = driver.find_elements_by_tag_name("img")
    images.append(img[0].get_attribute("src")) 

print('I scraped '+ str(len(images)) + ' images!')

path = os.getcwd()
path = os.path.join(path, "FB_IMAGES_SCRAPED")

#Tạo 1 file chứa ảnh
os.mkdir(path)

counter = 0
for image in images:
    save_as = os.path.join(path, str(counter) + '.jpg')
    wget.download(image, save_as)
    counter += 1
time.sleep(5)
#tải trang danh sách bạn bè
driver.get(facebook_user_profile_url+"/friends_all")
time.sleep(5)
#cuộn trang xuống
for j in range(0,1):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(10)
count=0
#tìm các elements với địa chỉ xpath có sẵn
friends = driver.find_elements_by_xpath("//span[@class='d2edcug0 hpfvmrgz qv66sw1b c1et5uql lr9zc1uh a8c37x1j fe6kdd0r mau55g9w c8b282yb keod5gw0 nxhoafnm aigsh9s9 d3f4x2em mdeji52x a5q79mjw g1cxx5fr lrazzd5p oo9gr5id']")
time.sleep(5)
print('\n')
print('\n')
#in ra danh sách bạn bè và tổng số bạn bè
print("****************_DANH SACH BAN BE_**************")
for a in friends:
    print(a.text)
    count+=1
print('================================================')
print('Tong: '+str(count))