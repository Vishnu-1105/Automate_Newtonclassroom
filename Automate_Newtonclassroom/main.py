import time
import datetime
import pause
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests


# noinspection PyStatementEffect
def internet() -> bool:
    try:
        requests.get('https://www.google.com/').status_code
        return True
    except:
        return False


def findDay() -> str:
    now = datetime.datetime.now()
    day = now.strftime("%A")
    return day


def googleMeet():
    urls = driver.find_elements_by_xpath('//*[@href]')
    meet = urls[-1].get_attribute('href')
    driver.get(meet)
    time.sleep(10)
    driver.find_element_by_xpath(
        '//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div[4]/div[1]/div/div/div').click()
    driver.find_element_by_xpath(
        '//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]/div/div[4]/div[2]/div/div').click()
    driver.find_element_by_xpath(
        '//*[@id="yDmH0d"]/c-wiz/div/div/div[8]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]/div[1]').click()
    time.sleep(5)


def login():
    day = findDay()
    today = datetime.date.today()
    if day == 'Monday':
        driver.find_element_by_xpath(
            '//*[@id="Class_weekTableId__2E750"]/div/div/div/div/div/div/div/div/table/tbody/tr[1]/td[2]/div').click()
        googleMeet()
        pause.until(datetime.datetime(today.year, today.month, today.day, 10, 5))
        driver.execute_script("window.history.go(-1)")
        time.sleep(15)
        driver.find_element_by_xpath(
            '//*[@id="Class_weekTableId__2E750"]/div/div/div/div/div/div/div/div/table/tbody/tr[1]/td[3]/div').click()
        googleMeet()
        pause.until(datetime.datetime(today.year, today.month, today.day, 11, 25))
        driver.execute_script("window.history.go(-1)")
        time.sleep(15)
        driver.find_element_by_xpath(
            '//*[@id="Class_weekTableId__2E750"]/div/div/div/div/div/div/div/div/table/tbody/tr[1]/td[5]/div').click()
        googleMeet()
        pause.until(datetime.datetime(today.year, today.month, today.day, 12, 30))
        driver.execute_script("window.history.go(-1)")
        time.sleep(15)
    elif day == 'Tuesday':
        driver.find_element_by_xpath(
            '//*[@id="Class_weekTableId__2E750"]/div/div/div/div/div/div/div/div/table/tbody/tr[2]/td[2]/div').click()
        googleMeet()
        pause.until(datetime.datetime(today.year, today.month, today.day, 10, 5))
        driver.execute_script("window.history.go(-1)")
        time.sleep(15)
        driver.find_element_by_xpath(
            '//*[@id="Class_weekTableId__2E750"]/div/div/div/div/div/div/div/div/table/tbody/tr[2]/td[3]/div').click()
        googleMeet()
        pause.until(datetime.datetime(today.year, today.month, today.day, 11, 25))
        driver.execute_script("window.history.go(-1)")
        time.sleep(15)
        driver.find_element_by_xpath(
            '//*[@id="Class_weekTableId__2E750"]/div/div/div/div/div/div/div/div/table/tbody/tr[2]/td[5]/div').click()
        googleMeet()
        pause.until(datetime.datetime(today.year, today.month, today.day, 12, 30))
        exit()
    elif day == 'Wednesday':
        driver.find_element_by_xpath(
            '//*[@id="Class_weekTableId__2E750"]/div/div/div/div/div/div/div/div/table/tbody/tr[3]/td[2]/div').click()
        googleMeet()
        pause.until(datetime.datetime(today.year, today.month, today.day, 10, 5))
        driver.execute_script("window.history.go(-1)")
        time.sleep(15)
        driver.find_element_by_xpath(
            '//*[@id="Class_weekTableId__2E750"]/div/div/div/div/div/div/div/div/table/tbody/tr[3]/td[3]/div').click()
        googleMeet()
        pause.until(datetime.datetime(today.year, today.month, today.day, 11, 25))
        driver.execute_script("window.history.go(-1)")
        time.sleep(15)
        driver.find_element_by_xpath(
            '//*[@id="Class_weekTableId__2E750"]/div/div/div/div/div/div/div/div/table/tbody/tr[3]/td[5]/div').click()
        googleMeet()
        pause.until(datetime.datetime(today.year, today.month, today.day, 12, 30))
        exit()
    elif day == 'Thursday':
        driver.find_element_by_xpath(
            '//*[@id="Class_weekTableId__2E750"]/div/div/div/div/div/div/div/div/table/tbody/tr[4]/td[2]/div').click()
        googleMeet()
        pause.until(datetime.datetime(today.year, today.month, today.day, 10, 5))
        driver.execute_script("window.history.go(-1)")
        time.sleep(15)
        driver.find_element_by_xpath(
            '//*[@id="Class_weekTableId__2E750"]/div/div/div/div/div/div/div/div/table/tbody/tr[4]/td[3]/div').click()
        googleMeet()
        pause.until(datetime.datetime(today.year, today.month, today.day, 11, 25))
        driver.execute_script("window.history.go(-1)")
        time.sleep(15)
        driver.find_element_by_xpath(
            '//*[@id="Class_weekTableId__2E750"]/div/div/div/div/div/div/div/div/table/tbody/tr[4]/td[5]/div').click()
        googleMeet()
        pause.until(datetime.datetime(today.year, today.month, today.day, 12, 30))
        exit()
    elif day == 'Friday':
        driver.find_element_by_xpath(
            '//*[@id="Class_weekTableId__2E750"]/div/div/div/div/div/div/div/div/table/tbody/tr[5]/td[2]/div').click()
        googleMeet()
        pause.until(datetime.datetime(today.year, today.month, today.day, 10, 5))
        driver.execute_script("window.history.go(-1)")
        time.sleep(15)
        driver.find_element_by_xpath(
            '//*[@id="Class_weekTableId__2E750"]/div/div/div/div/div/div/div/div/table/tbody/tr[5]/td[3]/div').click()
        googleMeet()
        pause.until(datetime.datetime(today.year, today.month, today.day, 11, 25))
        driver.execute_script("window.history.go(-1)")
        time.sleep(15)
        driver.find_element_by_xpath(
            '//*[@id="Class_weekTableId__2E750"]/div/div/div/div/div/div/div/div/table/tbody/tr[5]/td[5]/div').click()
        googleMeet()
        pause.until(datetime.datetime(today.year, today.month, today.day, 12, 30))
        exit()
    elif day == 'Saturday':
        driver.find_element_by_xpath(
            '//*[@id="Class_weekTableId__2E750"]/div/div/div/div/div/div/div/div/table/tbody/tr[6]/td[2]/div').click()
        googleMeet()
        pause.until(datetime.datetime(today.year, today.month, today.day, 10, 5))
        driver.execute_script("window.history.go(-1)")
        time.sleep(15)
        driver.find_element_by_xpath(
            '//*[@id="Class_weekTableId__2E750"]/div/div/div/div/div/div/div/div/table/tbody/tr[6]/td[3]/div').click()
        googleMeet()
        pause.until(datetime.datetime(today.year, today.month, today.day, 11, 25))
        driver.execute_script("window.history.go(-1)")
        time.sleep(15)
        driver.find_element_by_xpath(
            '//*[@id="Class_weekTableId__2E750"]/div/div/div/div/div/div/div/div/table/tbody/tr[6]/td[5]/div').click()
        googleMeet()
        pause.until(datetime.datetime(today.year, today.month, today.day, 12, 30))
        exit()


if not internet():
    print('Internet not connected')
    exit()

driver = webdriver.Chrome()
driver.get('https://griet.newtonclassroom.com')

driver.maximize_window()

signin = driver.find_element_by_xpath('//*[@id="Button_button__3GgJ3"]/a/div/div/span')
signin.click()

username = 'Your college e-mail'
password = 'Your e-mail password'

driver.find_element_by_xpath('//*[@id="identifierId"]').send_keys(username, Keys.ENTER)
time.sleep(4)
driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input').send_keys(password, Keys.ENTER)

time.sleep(15)

timetable = driver.find_element_by_xpath('//*[@id="layout_layout__vHTZi"]/div/div[1]/div/ul/li[4]/a')
timetable.click()

time.sleep(5)

login()
