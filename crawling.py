import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import traceback
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_text(soup):
    title = soup.find('th').text
    tbody = soup.find('tbody')
    tr_list = tbody.findAll('tr')
    phone = tr_list[2].findAll('td')[1].text
    attached = tr_list[4].findAll('td')[0]
    content = tr_list[6].findAll('td')[0].text.strip()
    return title, phone, content
    
def do_crawl():
    driver = webdriver.Firefox()#'./chromedriver')
    data = {'data':[]}
    delay = 5
    try:
        # 구글에 접속
        driver.get('https://www.sealife.go.kr/subject/support/list.do')

        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        tab = soup.find("table",{"class":"t_typelA listTypeA"})
        tbody = tab.find('tbody')
        tr_list = tbody.findAll('tr')#.find('td').find('td')
        for tr in tr_list:
            td = tr.find('td',{'class':'txt_left'})
            class_type = td.a.span.attrs['class'][0] # n1 or n2
            if class_type == 'n1':
                href = td.a.attrs['href']
                driver.execute_script(href)
                WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CLASS_NAME, 'contents')))
                html = driver.page_source
                soup = BeautifulSoup(html, 'html.parser')
                title, phone, content = get_text(soup)
                data['data'].append({'title':title,'phone':phone,'content':content})
                driver.execute_script("window.history.go(-1)")

    except:
        data = -1
        print("An exception occurred!")
        traceback.print_exc()
    finally:
        driver.quit()
        return data

if __name__ == '__main__':
    do_crawl()