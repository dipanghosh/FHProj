from selenium import webdriver
from bs4 import BeautifulSoup
import time


def getDepositDate(assayID):
    driver = webdriver.Firefox()
    url = "https://pubchem.ncbi.nlm.nih.gov/bioassay/"+str(assayID)
    driver.get(url)
    time.sleep(3)
    html_source = driver.page_source
    soup = BeautifulSoup(html_source,'html.parser')
    date = soup.find('span', {'class': 'date-item'}).text
    try:
        protocol = soup.find('li', {'id': 'Protocol'}).text
    except:
        protocol = '.'
    driver.quit()
    return (date, protocol)

def getAssayProtocol(assayID):
    driver = webdriver.Firefox()
    url = "https://pubchem.ncbi.nlm.nih.gov/bioassay/"+str(assayID)
    driver.get(url)
    time.sleep(3)
    html_source = driver.page_source
    soup = BeautifulSoup(html_source,'html.parser')
    date = soup.find('li', {'id': 'Protocol'}).text
    driver.quit()
    return date






