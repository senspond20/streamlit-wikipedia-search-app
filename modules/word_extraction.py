# from konlpy.tag import Kkma
# from konlpy.tag import Okt
import nltk
nltk.download('stopwords')
nltk.download('punkt')
from nltk.corpus import stopwords
from collections import Counter
from konlpy.tag import Komoran
import re

class WordExtraction():

    def __init__(self):
        self.mor = Komoran()

        # 불용어
        en_stop_words_list = stopwords.words('english')
        en_stop_words_list + ["the", "this", "are", "you","=","/","span"]
        self.kn_stop_words_list = ["모두", "안녕", "사실", "직접", "바탕", "위해", "나중", "브랜", "이름", "본래", "무엇","가지","은는","이가"]
        self.en_stop_words_list = en_stop_words_list

    def pre_processing(selt, text):
        """ 텍스트 전처리 """
        word = re.compile('[^가-힣A-Za-z]') # 한글,영어 아니면 전부 ' ' 로 치환
        result = word.sub(' ', text)
        return result


    def ko_extract(self, text, top=150):
        ftext = self.pre_processing(text)
        tokens = filter(lambda s: len(s) > 1 and str(s).lower() not in self.kn_stop_words_list, self.mor.nouns(ftext))
        count = Counter(tokens)
        return count.most_common(top)


    def en_extract(self, text, top=150):
        ftext = self.pre_processing(text)
        tokens = filter(lambda s: len(s) > 3 and str(s).lower() not in self.en_stop_words_list, nltk.word_tokenize(ftext))
        count = Counter(tokens)
        return count.most_common(top)


if __name__ == "__main__":
    from modules.wiki_search import WikiSearch, OutputFormat

    wiki = WikiSearch("ko", OutputFormat.WIKI)
    re_keyword, page = wiki.search("수학")

    w = WordExtraction()

    if page.exists():
        data = w.ko_extract(page.text)
        for item in data:
            print(item)

