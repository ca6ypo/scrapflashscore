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
        if count > 7:
            print("Timing out after 3 seconds and returning")
            return
        time.sleep(.5)
        try:
            elem == driver.find_element_by_tag_name("html")
        except StaleElementReferenceException:
            return

#REPLACE WITH YOUR DRIVER PATH. EXAMPLES FOR CHROME AND PHANTOMJS

urll = str(input("link please:"))
#urll = "https://www.flashscore.ru/football/italy/serie-a/results/"
driver = webdriver.Chrome(executable_path='./chromedriver')
#driver = webdriver.PhantomJS(executable_path='./phantomjs')
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
odd3om, odd3ob, odd3nm, odd3nb = [], [], [], []
resultss = []
komand = []
hahao1, hahao2, hahan1, hahan2 = [], [], [], []
btsoy, btson, btsny, btsnn = [], [], [], []
def prot(teams):
	komans = []
	for ssyl in teams:
		koman = ssyl.text
		komans.append(koman)
	print(str(komans[0]+"  :  "+komans[1]))
	komand.append(str(komans[0]+"  :  "+komans[1]))



def fodds2():
	driver.get(pink+"#odds-sammenligning/over-under/fuldtid")
	waitForLoad(driver)
	bsObj = BeautifulSoup(driver.page_source, 'lxml')
	odd05 = bsObj.find("div", {"id":"detail"}).find("div", {"class":"tableWrapper___33yhdWE"}).find_all("div", {"class":"table___21hYPOu odds___3BQPEof"})
	oddop = odd05[0].find("div", {"class":"row___1rtP1QI undefined"}).find_all("a", {"target":"_blank"})
	try:
		oddalt = re.findall(r'[-+]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][-+]?\d+)?', oddop[1].attrs["title"])
		odd0ob.append(oddalt[0])
		odd0nb.append(oddalt[1])
	except:
		oddalt = oddop[1].span.get_text()
		odd0ob.append(oddalt)
		odd0nb.append(oddalt)

	try:
		oddalt = re.findall(r'[-+]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][-+]?\d+)?', oddop[2].attrs["title"])
		odd0om.append(oddalt[0])
		odd0nm.append(oddalt[1])
	except:
		oddalt = oddop[2].span.get_text()
		odd0om.append(oddalt)
		odd0nm.append(oddalt)

	odd115 = int(input("insert place of 1.5   ---   "))
	odd15 = odd115 - 1
	oddop = odd05[odd15].find("div", {"class":"row___1rtP1QI undefined"}).find_all("a", {"target":"_blank"})
	try:
		oddalt = re.findall(r'[-+]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][-+]?\d+)?', oddop[1].attrs["title"])
		odd1ob.append(oddalt[0])
		odd1nb.append(oddalt[1])
	except:
		oddalt = oddop[1].span.get_text()
		odd1ob.append(oddalt)
		odd1nb.append(oddalt)

	try:
		oddalt = re.findall(r'[-+]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][-+]?\d+)?', oddop[2].attrs["title"])
		odd1om.append(oddalt[0])
		odd1nm.append(oddalt[1])
	except:
		oddalt = oddop[2].span.get_text()
		odd1om.append(oddalt)
		odd1nm.append(oddalt)

	odd225 = int(input("insert place of 2.5   ---   "))
	odd25 = odd225 - 1
	oddop = odd05[odd25].find("div", {"class":"row___1rtP1QI undefined"}).find_all("a", {"target":"_blank"})
	try:
		oddalt = re.findall(r'[-+]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][-+]?\d+)?', oddop[1].attrs["title"])
		odd2ob.append(oddalt[0])
		odd2nb.append(oddalt[1])
	except:
		oddalt = oddop[1].span.get_text()
		odd2ob.append(oddalt)
		odd2nb.append(oddalt)

	try:
		oddalt = re.findall(r'[-+]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][-+]?\d+)?', oddop[2].attrs["title"])
		odd2om.append(oddalt[0])
		odd2nm.append(oddalt[1])
	except:
		oddalt = oddop[2].span.get_text()
		odd2om.append(oddalt)
		odd2nm.append(oddalt)


	odd335 = int(input("insert place of 3.5   ---   "))
	odd35 = odd335 - 1
	oddop = odd05[odd35].find("div", {"class":"row___1rtP1QI undefined"}).find_all("a", {"target":"_blank"})
	try:
		oddalt = re.findall(r'[-+]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][-+]?\d+)?', oddop[1].attrs["title"])
		odd3ob.append(oddalt[0])
		odd3nb.append(oddalt[1])
	except:
		oddalt = oddop[1].span.get_text()
		odd3ob.append(oddalt)
		odd3nb.append(oddalt)

	try:
		oddalt = re.findall(r'[-+]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][-+]?\d+)?', oddop[2].attrs["title"])
		odd3om.append(oddalt[0])
		odd3nm.append(oddalt[1])
	except:
		oddalt = oddop[2].span.get_text()
		odd3om.append(oddalt)
		odd3nm.append(oddalt)


	print("going to h/u")
	driver.get(pink+"#odds-sammenligning/home-away/fuldtid")
	waitForLoad(driver)
	bsObj = BeautifulSoup(driver.page_source, 'lxml')
	odd05 = bsObj.find("div", {"id":"detail"}).find("div", {"class":"tableWrapper___33yhdWE"}).find("div", {"class":"table___21hYPOu odds___3BQPEof"})
	oddop = odd05.find("div", {"class":"row___1rtP1QI undefined"}).find_all("a", {"target":"_blank"})
	try:
		oddalt = re.findall(r'[-+]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][-+]?\d+)?', oddop[1].attrs["title"])
		hahao1.append(oddalt[0])
		hahan1.append(oddalt[1])
	except:
		oddalt = oddop[1].span.get_text()
		hahan1.append(oddalt)
		hahao1.append(oddalt)

	try:
		oddalt = re.findall(r'[-+]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][-+]?\d+)?', oddop[2].attrs["title"])
		hahao2.append(oddalt[0])
		hahan2.append(oddalt[1])
	except:
		oddalt = oddop[2].span.get_text()
		hahao2.append(oddalt)
		hahan2.append(oddalt)

	print("going to bhs")
	driver.get(pink+"#odds-sammenligning/begge-hold-scorer/fuldtid")
	waitForLoad(driver)
	bsObj = BeautifulSoup(driver.page_source, 'lxml')
	odd05 = bsObj.find("div", {"id":"detail"}).find("div", {"class":"tableWrapper___33yhdWE"}).find("div", {"class":"table___21hYPOu odds___3BQPEof"})
	oddop = odd05.find("div", {"class":"row___1rtP1QI undefined"}).find_all("a", {"target":"_blank"})
	try:
		oddalt = re.findall(r'[-+]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][-+]?\d+)?', oddop[1].attrs["title"])
		btsoy.append(oddalt[0])
		btsny.append(oddalt[1])
	except:
		oddalt = oddop[1].span.get_text()
		btsoy.append(oddalt)
		btsny.append(oddalt)

	try:
		oddalt = re.findall(r'[-+]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][-+]?\d+)?', oddop[2].attrs["title"])
		btson.append(oddalt[0])
		btsnn.append(oddalt[1])
	except:
		oddalt = oddop[2].span.get_text()
		btson.append(oddalt)
		btsnn.append(oddalt)




def fodds():
	# driver.find("a", {"class":"tabs__tab"}).click()
	# waitForLoad(driver)
	# #bsObj = BeautifulSoup(driver.page_source, 'lxml')
	# driver.find_element_by_id('bookmark-under-over').click()
	driver.get(pink+"#odds-sammenligning/over-under/fuldtid")
	#waitForLoad(driver)
	bsObj = BeautifulSoup(driver.page_source, 'lxml')
	print(bsObj.text + "\n" + "\n" + "\n")
	odd05 = bsObj.find("div", {"id":"detail"}).div.find("div", {"class":"tableWrapper___33yhdWE"}).find("div", {"class":"table___21hYPOu odds___3BQPEof"}).find("div", {"class":"rows___1BdItrT"}).find("div", {"class":"row___1rtP1QI undefined"}).find("a", {"class":"odd___2vKX0U5  "})
	#odd0.append(odd05.attrs["alt"]) <a class="odd___2vKX0U5 highlight___14W_vkK " href="/bookmaker/16/?from=odds-comparison&sport=1&gicc=CZ&gisc=CZ-10" target="_blank" title>
	try:
		print(odd05 + "\n")
		oddalt = re.split(r' » ', odd05.attrs["title"])
		odd0ob.append(oddalt[0])
		odd0nb.append(oddalt[1])
		print("split proshel")
	except:
		odd0ob.append(odd05.get_text())
		odd0nb.append(odd05.get_text())
	odd05 = bsObj.find("div", {"id":"detail"}).div.find("div", {"class":"tableWrapper___33yhdWE"}).find("div", {"class":"table___21hYPOu odds___3BQPEof"}).find("div", {"class":"rows___1BdItrT"}).find("div", {"class":"row___1rtP1QI undefined"}).find("a", {"class":"odd___2vKX0U5 highlight___14W_vkK "})
	try:
		oddalt = re.findall(r'[-+]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][-+]?\d+)?', odd05.attrs["title"])
		odd0om.append(oddalt[0])
		odd0nm.append(oddalt[1])
	except:
		odd0om.append(odd05.get_text())
		odd0nm.append(odd05.get_text())
	odd05 = bsObj.find("table", {"id":"odds_ou_1.5"}).tbody.find("tr", {"class":"odd"}).find("td", {"onclick":"e_t.track_click('CLICK_ODD', 'block-under-over_ft_over');"}).span
	#odd0.append(odd05.attrs["alt"])
	try:
		oddalt = re.findall(r'[-+]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][-+]?\d+)?', odd05.attrs["title"])
		odd1ob.append(oddalt[0])
		odd1nb.append(oddalt[1])
	except:
		odd1ob.append(odd05.get_text())
		odd1nb.append(odd05.get_text())
	odd05 = bsObj.find("table", {"id":"odds_ou_1.5"}).tbody.find("tr", {"class":"odd"}).find("td", {"onclick":"e_t.track_click('CLICK_ODD', 'block-under-over_ft_under');"}).span
	try:
		oddalt = re.findall(r'[-+]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][-+]?\d+)?', odd05.attrs["title"])
		odd1om.append(oddalt[0])
		odd1nm.append(oddalt[1])
	except:
		odd1om.append(odd05.get_text())
		odd1nm.append(odd05.get_text())
	odd05 = bsObj.find("table", {"id":"odds_ou_2.5"}).tbody.find("tr", {"class":"odd"}).find("td", {"onclick":"e_t.track_click('CLICK_ODD', 'block-under-over_ft_over');"}).span
	#odd0.append(odd05.attrs["alt"])
	try:
		oddalt = re.findall(r'[-+]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][-+]?\d+)?', odd05.attrs["title"])
		odd2ob.append(oddalt[0])
		odd2nb.append(oddalt[1])
	except:
		odd2ob.append(odd05.get_text())
		odd2nb.append(odd05.get_text())
	odd05 = bsObj.find("table", {"id":"odds_ou_2.5"}).tbody.find("tr", {"class":"odd"}).find("td", {"onclick":"e_t.track_click('CLICK_ODD', 'block-under-over_ft_under');"}).span
	try:
		oddalt = re.findall(r'[-+]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][-+]?\d+)?', odd05.attrs["title"])
		odd2om.append(oddalt[0])
		odd2nm.append(oddalt[1])
	except:
		odd2om.append(odd05.get_text())
		odd2nm.append(odd05.get_text())
	#print("DABLYAT")
	odd05 = bsObj.find("table", {"id":"odds_ou_3.5"}).tbody.find("tr", {"class":"odd"}).find("td", {"onclick":"e_t.track_click('CLICK_ODD', 'block-under-over_ft_over');"}).span
	#odd0.append(odd05.attrs["alt"])
	try:
		oddalt = re.findall(r'[-+]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][-+]?\d+)?', odd05.attrs["title"])
		odd3ob.append(oddalt[0])
		odd3nb.append(oddalt[1])
	except:
		odd3ob.append(odd05.get_text())
		odd3nb.append(odd05.get_text())
	odd05 = bsObj.find("table", {"id":"odds_ou_3.5"}).tbody.find("tr", {"class":"odd"}).find("td", {"onclick":"e_t.track_click('CLICK_ODD', 'block-under-over_ft_under');"}).span
	try:
		oddalt = re.findall(r'[-+]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][-+]?\d+)?', odd05.attrs["title"])
		odd3om.append(oddalt[0])
		odd3nm.append(oddalt[1])
	except:
		odd3om.append(odd05.get_text())
		odd3nm.append(odd05.get_text())
	driver.find_element_by_id('bookmark-moneyline').click()
	bsObj = BeautifulSoup(driver.page_source, 'lxml')
	odd05 = bsObj.find("table", {"id":"odds_dnb"}).tbody.find("tr", {"class":"odd"}).find("td", {"onclick":"e_t.track_click('CLICK_ODD', 'block-moneyline_ft_1');"}).span
	try:
		oddalt = re.findall(r'[-+]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][-+]?\d+)?', odd05.attrs["title"])
		hahao1.append(oddalt[0])
		hahan1.append(oddalt[1])
	except:
		hahao1.append(odd05.get_text())
		hahan1.append(odd05.get_text())
	odd05 = bsObj.find("table", {"id":"odds_dnb"}).tbody.find("tr", {"class":"odd"}).find("td", {"onclick":"e_t.track_click('CLICK_ODD', 'block-moneyline_ft_2');"}).span
	try:
		oddalt = re.findall(r'[-+]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][-+]?\d+)?', odd05.attrs["title"])
		hahao2.append(oddalt[0])
		hahan2.append(oddalt[1])
	except:
		hahao2.append(odd05.get_text())
		hahan2.append(odd05.get_text())

	driver.find_element_by_id('bookmark-both-teams-to-score').click()
	bsObj = BeautifulSoup(driver.page_source, 'lxml')
	odd05 = bsObj.find("table", {"id":"odds_both_teams_to_score"}).tbody.find("tr", {"class":"odd"}).find("td", {"onclick":"e_t.track_click('CLICK_ODD', 'block-both-teams-to-score_ft_yes');"}).span
	try:
		oddalt = re.findall(r'[-+]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][-+]?\d+)?', odd05.attrs["title"])
		btsoy.append(oddalt[0])
		btsny.append(oddalt[1])
	except:
		btsoy.append(odd05.get_text())
		btsny.append(odd05.get_text())
	odd05 = bsObj.find("table", {"id":"odds_both_teams_to_score"}).tbody.find("tr", {"class":"odd"}).find("td", {"onclick":"e_t.track_click('CLICK_ODD', 'block-both-teams-to-score_ft_no');"}).span
	try:
		oddalt = re.findall(r'[-+]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][-+]?\d+)?', odd05.attrs["title"])
		btson.append(oddalt[0])
		btsnn.append(oddalt[1])
	except:
		btson.append(odd05.get_text())
		btsnn.append(odd05.get_text())
	#print(odd0ob, odd1ob, odd2ob)
	#print(odd0ob, odd1ob, odd2ob)

def goParse(pink):
	driver.get(pink)
	waitForLoad(driver)
	bsObj = BeautifulSoup(driver.page_source, 'lxml')
	tour = bsObj.find("div", {"class":"description___3_uvNAG tournamentHeaderDescription"}).div.find("span", {"class":"country___24Qe-aj"}).text
	tourss.append(tour)
	result = bsObj.find("div", {"class":"wrapper___3rU3Jah"}).text
	resultss.append(result)
	teams = bsObj.find_all("div", {"class":"participantNameWrapper___3cGNQoU"})
	prot(teams)
	time1 = bsObj.find("div", {"class":"incidentsHeader___7PI0XDi"})
	tme1 = time1.find_all("div")
	tie1 = tme1[1].text
	tim1.append(tie1)
	#print("ADBLYAT" + tie1)
	#print(tour, result, teams, tie1)
	fodds2()

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
	df['H/Ao1'] = hahao1
	df['H/Ao2'] = hahao2
	df['H/An1'] = hahan1
	df['H/An2'] = hahan2
	df['0,5 oo'] = odd0ob
	df['0,5 ou'] = odd0om
	df['0,5 no'] = odd0nb
	df['0,5 nu'] = odd0nm
	df['1,5 oo'] = odd1ob
	df['1,5 ou'] = odd1om
	df['1,5 no'] = odd1nb
	df['1,5 nu'] = odd1nm
	df['2,5 oo'] = odd2ob
	df['2,5 ou'] = odd2om
	df['2,5 no'] = odd2nb
	df['2,5 nu'] = odd2nm
	df['BTS oY'] = btsoy
	df['BTS oN'] = btson
	df['BTS nY'] = btsny
	df['BTS nn'] = btsnn
	df['3,5 oo'] = odd3ob
	df['3,5 ou'] = odd3om
	df['3,5 no'] = odd3nb
	df['3,5 nu'] = odd3nm
	writer = pandas.ExcelWriter('./sheet.xlsx', engine='xlsxwriter')
	df.to_excel(writer, sheet_name='listperviy', index=False)

	writer.sheets['listperviy'].set_column('A:A', 15)
	writer.sheets['listperviy'].set_column('B:B', 25)
	writer.sheets['listperviy'].set_column('C:C', 25)
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
	writer.sheets['listperviy'].set_column('Z:Z', 5)
	writer.sheets['listperviy'].set_column('AA:AA', 5)
	writer.sheets['listperviy'].set_column('AB:AB', 5)
	writer.sheets['listperviy'].set_column('AC:AC', 5)
	writer.save()

print("start_TO_excel")
toxls()

