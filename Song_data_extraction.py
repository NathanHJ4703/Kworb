import requests
from bs4 import BeautifulSoup

URL = "https://kworb.net/youtube/insights/au_daily.html"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id="dailytable")

songs = results.find("tbody")
song_rankings = songs.find_all("tr")

for song in song_rankings:
	row_data = song.find_all("td")
	rank = row_data[0].text.strip()
	rank_change = row_data[1].text.strip()
	artist = row_data[2].text.strip()
	print(artist)
	print()
