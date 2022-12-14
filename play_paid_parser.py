#play_paid_parser.py
from bs4 import BeautifulSoup
import requests
#from Game import Game        #외부모듈만들기 전
from jputils.Game import Game  # from (패키지폴더 jputils) (모듈파일 Game) import (Game 클래스)


url = "https://play.google.com/store/apps/category/GAME/collection/topselling_paid"
res = requests.get(url)
# print(res.text)
# exit()
soup = BeautifulSoup(res.text, 'html.parser')
# card_list = soup.select('div.card-list')       #조부모 태그객체 card-list의 리스트, 1개 나옴
card_list = soup.select('body')
# print(card_list)
# exit()
print(">>>>>>>>>",len(card_list), card_list[0].get('class'), type(card_list[0]))   
games=[]
for i in card_list:                       # 조부모태그객체 card-list 의 리스트, 1개 있음
    cards = i.select('.card')             # 부모태그객체 card의 리스트, 60개 나옴
    print('>>>', len(cards))              # 부모태그객체 갯수 60개나옴


    isDebug = True                        # QQQ (배포시 수정 할곳 마킹, False)
    tmpi=0
    for c in cards:                       # 각 카드별로= 부모태그 별로
        if isDebug:
            tmpi += 1
            if tmpi > 10: break               # 테스트 할떄는 10개만
        games.append(Game(c))             # 각 카드별로 작업 = 부모태그별로 작업

for i in games:
    print(i)

with open('games.csv','w',encoding='utf-8') as file:     #'utf-8'은 윈도우라서 써줘야됨
    file.write('game\tcomp\tprice\trating\n')
    for i in games:
        file.write(i.to_str() + '\n')                #Game 인스털스를 쓸수 없으므로 to.str 함수 만들어서 쓴다