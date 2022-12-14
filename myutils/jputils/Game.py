#Game.py
class Game:
    title = ''
    def __init__(self,parent_tag):
            #self.title = parent_tag.select('a.title')[0].text.strip()        #카드 태그 c 에서 a태크title클래스 가져와 텍스트 부르기 -> 아래 함수로 대체
            ##self.title = parent_tag.select('a.subtitle')[0].get('title')    #카드 태그 c에서 a태그subtitle클래스 가져와 title attribute 가져오기 -> 아래 함수로 대체
            self.title = self.get_text(parent_tag, 'a.title')
            self.comp = self.get_attr(parent_tag, 'a.subtitle', 'title') 
            self.price = self.get_text(parent_tag, 'span.current-price')
            self.rating = self.get_rating(parent_tag, 'div.current-rating', 'style')
    def get_rating(self, parent_tag, targ_selector, targ_attr_name):
        rating_style = self.get_attr(parent_tag, targ_selector, targ_attr_name)
        percent_num = float(rating_style.split(' ')[1].replace('%;', ''))   # rating style 스플릿한 값이 작아서 인덱스 에러 나는 경우 수정추가 해야 됨, len(rating_style.split(' '))<2 면 0.0 리턴
        return percent_num
    def get_text(self, parent_tag, targ_selector):
        targ_tag = self.get_targ_tag(parent_tag, targ_selector)
        return targ_tag.text.strip()   # .text 는 html 아닌 "" 안의 문자열
    def get_attr(self, parent_tag, targ_selector, targ_attr_name):
        targ_tag = self.get_targ_tag(parent_tag, targ_selector)
        return targ_tag.get(targ_attr_name).strip()
    def get_targ_tag(self, parent_tag, targ_selector):              #부모태그로 타겟태그 구함
        targ_tag = parent_tag.select(targ_selector)
        return None if targ_tag == None or len(targ_tag)==0 else targ_tag       # 리스트 아닌 형태로 받으려고 [0], 어짜피 1개일수도
    def __str__(self):
        self.to_str()
    def to_str(self):
        return '{}\t{}\t{}\t{:.1f}'.format(self.title, self.comp,self.price, self.rating)
        
if __name__ == '__main__':
    print("============", __name__)