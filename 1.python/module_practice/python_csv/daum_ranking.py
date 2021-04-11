import requests
import csv
from bs4 import BeautifulSoup
from pprint import pprint


daum_url = 'https://www.daum.net/'
response = requests.get(daum_url).text
data = BeautifulSoup(response, 'html.parser')

rankings = data.select('#mArticle > div.cmain_tmp > div.section_media > div.hotissue_builtin > div.realtime_part > ol > li > div > div:nth-child(1) > span.txt_issue > a') # 여러개를 가져올 때
#pprint(rankings)
for idx, rank in enumerate(rankings, 1):
    print(f'{idx}위 : {rank.text}')

# result_dict = {}
# for idx, rank in enumerate(rankings, 1):
#     result_dict[f'{idx}위'] = f'{rank.text}'

# with open('daum_rank.csv', 'w', newline='', encoding='utf-8') as csvfile:
#     csv_writer = csv.writer(csvfile)
#     for item, rank in result_dict.items():
#         csv_writer.writerow([item, rank])
    
#데이터를 json Data처럼 다시만들기 
result_list = []
for idx, rank in enumerate(rankings, 1):
    result_dict = {'rank': f'{idx}위', 'ranker': rank.text}
    result_list.append(result_dict)
# pprint(result_list)

#dict writer 만 쓸줄 알면 된다.!

with open('daum_rank.csv', 'w', newline='', encoding='utf-8') as csvfile:
    #field name을 작성할때는 딕셔너리의 키값과 동일하게 지정해야함.
    fieldnames = ['rank', 'ranker']
    csv_writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
    #필드네임을 csv 파일 최상단에 작성함.
    csv_writer.writeheader()
    # 리스트를 순회하며 key(csv의 필드)를 통해 value(내용)을 작성한다.
    for item in result_list:
        csv_writer.writerow(item)
    