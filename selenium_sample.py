from selenium import webdriver
import time


if __name__ == '__main__':
    user = ''
    pwd = ''

    driver = webdriver.Chrome(executable_path='./chromedriver.exe')
    driver.implicitly_wait(10)  # set implicit wait after every action
    driver.get('https://www.facebook.com')

    driver.maximize_window()  # maximize browser window
    time.sleep(2)  # wait
    driver.find_element_by_id("email").send_keys(user)  # set user name to the field
    driver.find_element_by_id("pass").send_keys(pwd)  # set password to the field
    # click log in button
    submit_button = driver.find_elements_by_xpath('//*[@id="u_0_8"]')[0]
    submit_button.click()

    time.sleep(2)  # wait
    # driver.close()
    driver.quit()
