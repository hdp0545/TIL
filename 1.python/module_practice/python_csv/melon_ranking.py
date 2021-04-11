import requests
from bs4 import BeautifulSoup
import csv


melon_url = 'https://www.melon.com/chart/index.htm'
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}
response = requests.get(melon_url, headers = headers).text
data = BeautifulSoup(response, 'html.parser')
songs = data.select('#lst50')
# singer = data.select('#lst50 > td > div > div > div.ellipsis.rank02 > a')
# rankings = data.select('#lst50 > td > div > div > div.ellipsis.rank01 > span > a')
# 순위, 가수, 노래제목을 포함하는 요소를 먼저 크게 선택 후
# 반복을 돌면서 순위, 가수, 노래제목을 하나만 다시 선택.
result_list = []
for song in songs:
    rank = song.select_one('td:nth-child(2) > div > span.rank').text
    title = song.select_one('td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a').text
    artist = song.select_one('td:nth-child(6) > div > div > div.ellipsis.rank02 > a').text
    item = {'rank': rank, 'title': title, 'artist': artist}
    result_list.append(item)


with open('melon_result.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['rank', 'artist', 'title']
    csv_writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
    csv_writer.writeheader()
    for item in result_list:
        csv_writer.writerow(item)
