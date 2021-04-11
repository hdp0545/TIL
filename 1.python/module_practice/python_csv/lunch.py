import csv

lunch = {
    '양자강': '02-111-2222',
    '김밥까페': '02-333-4444',
    '순남시레기': '02-555-6666',
}

#파일을 열어야 함.
#open내장함수로 해당 파일을 열고 파일 객체를 만든다.
#newline이 윈도우에서는 \n이 기본값. 엔터가 2번 쳐진다.
#encoding이 윈도우에서는 cp949가 기본값 utf-8로 바꾼다.
with open('lunch.csv', 'w', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile)
    for item, number in lunch.items():
        csv_writer.writerow([item, number])

#파일 조작이 끝나면 반드시 닫아야 한다.

