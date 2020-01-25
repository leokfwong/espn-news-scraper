import requests
from bs4 import BeautifulSoup
import time
import random

#ids_2018 = range(400975296, 400975506)
ids_2019 = range(401071360, 401071442)

# Iterate through IDs
for id in ids_2019:
	# Fetch content from article
	URL = 'https://www.espn.com/nba/recap?gameId=' + str(id)
	page = requests.get(URL)
	soup = BeautifulSoup(page.content, 'html.parser')
	results = soup.find(id='article-feed')
	# If content found
	if len(results) > 0:
		# Fetch title of recap
		title = results.find_all('header', class_='article-header')
		if len(title) > 0:
			with open("data/espn_2019.txt", "a") as outfile:
				outfile.write(title[0].text + "\n")
		# Fetch content of recap
		elems = results.find_all('p')
		if len(elems) > 0:
			for elem in elems:
				with open("data/espn_2019.txt", "a") as outfile:
					outfile.write(elem.text + "\n")
	# Generate random pause
	pause = random.randint(10, 30)
	print("Fetched " + str(id) + ", sleeping for " + str(pause) + " seconds.")
	time.sleep(pause)