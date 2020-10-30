from selenium import webdriver
import time
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import StaleElementReferenceException

import re 
import requests
from bs4 import BeautifulSoup
import xlrd
import pandas

def waitForLoad(driver):
    elem = driver.find_element_by_tag_name("html")
    count = 0
    while True:
        count += 1
        if count > 20:
            print("Timing out after 10 seconds and returning")
            return
        time.sleep(.5)
        try:
            elem == driver.find_element_by_tag_name("html")
        except StaleElementReferenceException:
            return


urll = str(input("link please:"))
#urll = "https://www.flashscore.ru/football/italy/serie-a/results/"
driver = webdriver.Chrome(executable_path='./chromedriver')
driver.get(urll)
waitForLoad(driver)
#print(driver.page_source)


bsObj = BeautifulSoup(driver.page_source, "lxml")

chis = int(input("how many:"))
links = []
#global links
matches = bsObj.find_all("div", {"class":"event__match"}, limit=chis)
for match in matches:
	print(match.get_text(), "   ", match.attrs["id"])
	link = match.attrs["id"]
	links.append(link)

tourss = []
tot, tim1 = [], []
odd0, odd0om, odd0ob, odd0nb, odd0nm, odd1om, odd1ob, odd1nm, odd1nb, odd2om, odd2ob, odd2nm, odd2nb = [],[], [], [],[], [], [],[], [], [],[], [], []
resultss = []
komand = []
hahao1, hahao2, hahan1, hahan2 = [], [], [], []
btsoy, btson, btsny, btsnn = [], [], [], []
def prot(teams):
	komans = []
	for ssyl in teams:
		koman = ssyl.get_text()
		komans.append(koman)
	komand.append(str(komans[0]+"  :  "+komans[1]))

def fodds():
	driver.find_element_by_id('a-match-odds-comparison').click()
	waitForLoad(driver)
	#bsObj = BeautifulSoup(driver.page_source, 'lxml')
	driver.find_element_by_id('bookmark-under-over').click()
	bsObj = BeautifulSoup(driver.page_source, 'lxml')
	odd05 = bsObj.find("table", {"id":"odds_ou_0.5"}).tbody.find("tr", {"class":"odd"}).find("td", {"onclick":"e_t.track_click('bookmaker-button-click', 'block-under-over_ft_over');"}).span
	#odd0.append(odd05.attrs["alt"])
	try:
		oddalt = re.findall(r'[-+]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][-+]?\d+)?', odd05.attrs["alt"])
		odd0ob.append(oddalt[0])
		odd0nb.append(oddalt[1])
	except:
		odd0ob.append(odd05.get_text())
		odd0nb.append(odd05.get_text())
	odd05 = bsObj.find("table", {"id":"odds_ou_0.5"}).tbody.find("tr", {"class":"odd"}).find("td", {"onclick":"e_t.track_click('bookmaker-button-click', 'block-under-over_ft_under');"}).span
	try:
		oddalt = re.findall(r'[-+]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][-+]?\d+)?', odd05.attrs["alt"])
		odd0om.append(oddalt[0])
		odd0nm.append(oddalt[1])
	except:
		odd0om.append(odd05.get_text())
		odd0nm.append(odd05.get_text())
	odd05 = bsObj.find("table", {"id":"odds_ou_1.5"}).tbody.find("tr", {"class":"odd"}).find("td", {"onclick":"e_t.track_click('bookmaker-button-click', 'block-under-over_ft_over');"}).span
	#odd0.append(odd05.attrs["alt"])
	try:
		oddalt = re.findall(r'[-+]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][-+]?\d+)?', odd05.attrs["alt"])
		odd1ob.append(oddalt[0])
		odd1nb.append(oddalt[1])
	except:
		odd1ob.append(odd05.get_text())
		odd1nb.append(odd05.get_text())
	odd05 = bsObj.find("table", {"id":"odds_ou_1.5"}).tbody.find("tr", {"class":"odd"}).find("td", {"onclick":"e_t.track_click('bookmaker-button-click', 'block-under-over_ft_under');"}).span
	try:
		oddalt = re.findall(r'[-+]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][-+]?\d+)?', odd05.attrs["alt"])
		odd1om.append(oddalt[0])
		odd1nm.append(oddalt[1])
	except:
		odd1om.append(odd05.get_text())
		odd1nm.append(odd05.get_text())
	odd05 = bsObj.find("table", {"id":"odds_ou_2.5"}).tbody.find("tr", {"class":"odd"}).find("td", {"onclick":"e_t.track_click('bookmaker-button-click', 'block-under-over_ft_over');"}).span
	#odd0.append(odd05.attrs["alt"])
	try:
		oddalt = re.findall(r'[-+]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][-+]?\d+)?', odd05.attrs["alt"])
		odd2ob.append(oddalt[0])
		odd2nb.append(oddalt[1])
	except:
		odd2ob.append(odd05.get_text())
		odd2nb.append(odd05.get_text())
	odd05 = bsObj.find("table", {"id":"odds_ou_2.5"}).tbody.find("tr", {"class":"odd"}).find("td", {"onclick":"e_t.track_click('bookmaker-button-click', 'block-under-over_ft_under');"}).span
	try:
		oddalt = re.findall(r'[-+]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][-+]?\d+)?', odd05.attrs["alt"])
		odd2om.append(oddalt[0])
		odd2nm.append(oddalt[1])
	except:
		odd2om.append(odd05.get_text())
		odd2nm.append(odd05.get_text())
	print("DABLYAT")
	driver.find_element_by_id('bookmark-moneyline').click()
	bsObj = BeautifulSoup(driver.page_source, 'lxml')
	odd05 = bsObj.find("table", {"id":"odds_dnb"}).tbody.find("tr", {"class":"odd"}).find("td", {"onclick":"e_t.track_click('bookmaker-button-click', 'block-moneyline_ft_1');"}).span
	try:
		oddalt = re.findall(r'[-+]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][-+]?\d+)?', odd05.attrs["alt"])
		hahao1.append(oddalt[0])
		hahan1.append(oddalt[1])
	except:
		hahao1.append(odd05.get_text())
		hahan1.append(odd05.get_text())
	odd05 = bsObj.find("table", {"id":"odds_dnb"}).tbody.find("tr", {"class":"odd"}).find("td", {"onclick":"e_t.track_click('bookmaker-button-click', 'block-moneyline_ft_2');"}).span
	try:
		oddalt = re.findall(r'[-+]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][-+]?\d+)?', odd05.attrs["alt"])
		hahao2.append(oddalt[0])
		hahan2.append(oddalt[1])
	except:
		hahao2.append(odd05.get_text())
		hahan2.append(odd05.get_text())

	driver.find_element_by_id('bookmark-both-teams-to-score').click()
	bsObj = BeautifulSoup(driver.page_source, 'lxml')
	odd05 = bsObj.find("table", {"id":"odds_both_teams_to_score"}).tbody.find("tr", {"class":"odd"}).find("td", {"onclick":"e_t.track_click('bookmaker-button-click', 'block-both-teams-to-score_ft_yes');"}).span
	try:
		oddalt = re.findall(r'[-+]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][-+]?\d+)?', odd05.attrs["alt"])
		btsoy.append(oddalt[0])
		btsny.append(oddalt[1])
	except:
		btsoy.append(odd05.get_text())
		btsny.append(odd05.get_text())
	odd05 = bsObj.find("table", {"id":"odds_both_teams_to_score"}).tbody.find("tr", {"class":"odd"}).find("td", {"onclick":"e_t.track_click('bookmaker-button-click', 'block-both-teams-to-score_ft_no');"}).span
	try:
		oddalt = re.findall(r'[-+]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][-+]?\d+)?', odd05.attrs["alt"])
		btson.append(oddalt[0])
		btsnn.append(oddalt[1])
	except:
		btson.append(odd05.get_text())
		btsnn.append(odd05.get_text())

def goParse(pink):
	driver.get(pink)
	waitForLoad(driver)
	bsObj = BeautifulSoup(driver.page_source, 'lxml')
	tour = bsObj.find("div", {"class":"description__match"})
	tourss.append(tour.get_text())
	result = bsObj.find("div", {"class":"current-result"})
	resultss.append(result.get_text())
	teams = bsObj.find_all("div", {"class":"tname__text"})
	prot(teams)
	time1 = bsObj.find("div", {"class":"detailMS__headerScore"})
	tim1.append(time1.get_text())
	#print("ADBLYAT")
	fodds()

pinks = []
for pink in links:
	pink = re.sub(r'g_1_', 'https://flashscore.dk/kamp/', pink)
	pinks.append(pink)
	print(pink)
	goParse(pink)
	#print(komand, tourss, resultss, tim1)

def make_hyperlink(komand, pink):
	return '=HYPERLINK("%s", "%s")'%(pink.format(pink), komand)

def toxls():
	df = pandas.DataFrame()
	df['link'] = pinks
	df['Teams'] = komand
	df['tour - league'] = tourss
	df['first time res'] = tim1
	df['results'] = resultss
	df['0,5 oo'] = odd0ob
	df['0,5 no'] = odd0nb
	df['0,5 ou'] = odd0om
	df['0,5 nu'] = odd0nm
	df['1,5 oo'] = odd1ob
	df['1,5 no'] = odd1nb
	df['1,5 ou'] = odd1om
	df['1,5 nu'] = odd1nm
	df['2,5 oo'] = odd2ob
	df['2,5 no'] = odd2nb
	df['2,5 ou'] = odd2om
	df['2,5 nu'] = odd2nm
	df['H/Ao1'] = hahao1
	df['H/An1'] = hahan1
	df['H/Ao2'] = hahao2
	df['H/An2'] = hahan2
	df['BTS oY'] = btsoy
	df['BTS nY'] = btsny
	df['BTS oN'] = btson
	df['BTS nn'] = btsnn
	writer = pandas.ExcelWriter('./shit.xlsx', engine='xlsxwriter')
	df.to_excel(writer, sheet_name='listperviy', index=False)

	writer.sheets['listperviy'].set_column('A:A', 15)
	writer.sheets['listperviy'].set_column('B:B', 30)
	writer.sheets['listperviy'].set_column('C:C', 30)
	writer.sheets['listperviy'].set_column('D:D', 7)
	writer.sheets['listperviy'].set_column('E:E', 7)
	writer.sheets['listperviy'].set_column('F:F', 5)
	writer.sheets['listperviy'].set_column('G:G', 5)
	writer.sheets['listperviy'].set_column('H:H', 5)
	writer.sheets['listperviy'].set_column('I:I', 5)
	writer.sheets['listperviy'].set_column('J:J', 5)
	writer.sheets['listperviy'].set_column('K:K', 5)
	writer.sheets['listperviy'].set_column('L:L', 5)
	writer.sheets['listperviy'].set_column('M:M', 5)
	writer.sheets['listperviy'].set_column('N:N', 5)
	writer.sheets['listperviy'].set_column('O:O', 5)
	writer.sheets['listperviy'].set_column('P:P', 5)
	writer.sheets['listperviy'].set_column('Q:Q', 5)
	writer.sheets['listperviy'].set_column('R:R', 5)
	writer.sheets['listperviy'].set_column('S:S', 5)
	writer.sheets['listperviy'].set_column('T:T', 5)
	writer.sheets['listperviy'].set_column('U:U', 5)
	writer.sheets['listperviy'].set_column('V:V', 5)
	writer.sheets['listperviy'].set_column('W:W', 5)
	writer.sheets['listperviy'].set_column('X:X', 5)
	writer.sheets['listperviy'].set_column('Y:Y', 5)
	writer.save()

print("start_TO_excel")
toxls()

