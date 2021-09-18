from selenium import webdriver
import time


driver = webdriver.Firefox('C:/Users/jq/PycharmProjects/pythonProject')
driver.get('https://web-vpn.sues.edu.cn/')
driver.find_element_by_xpath('//*[@id="username"]').send_keys("081520105")
driver.find_element_by_xpath('//*[@id="password"]').send_keys('Fm1959286581')
driver.find_element_by_xpath('//*[@id="passbutton"]').click()
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div[4]/div[2]/div/div[2]/p[2]').click()
for handle in driver.window_handles:#方法二，始终获得当前最后的窗口，所以多要多次使用
    driver.switch_to.window(handle)
time.sleep(2)
driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[1]/div[2]/div/form/div[18]/div[1]/div/div[2]/div/div/input').send_keys("36.8")
driver.find_element_by_xpath('//*[@id="post"]').click()
time.sleep(2)
driver.quit()
