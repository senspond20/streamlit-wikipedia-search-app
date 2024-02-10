# from konlpy.tag import Kkma
# from konlpy.tag import Okt
import nltk
import ssl
from nltk.corpus import stopwords
from collections import Counter
from konlpy.tag import Komoran
import re


def nltk_download():
    # [nltk_data] Error loading stopwords: <urlopen error [SSL:
    try:
        _create_unverified_https_context = ssl._create_unverified_context
    except AttributeError:
        pass
    else:
        ssl._create_default_https_context = _create_unverified_https_context

    # 서버에서 없으며 오류가 남
    nltk.download('stopwords')
    nltk.download('punkt')


nltk_download()


class WordExtraction():

    def __init__(self):
        self.mor = Komoran()

        # 불용어
        en_stop_words_list = stopwords.words('english')
        en_stop_words_list + ["the", "this", "are", "you", "=", "/", "span"]
        self.kn_stop_words_list = ["모두", "안녕", "사실", "직접", "바탕", "위해", "나중", "브랜", "이름",
                                   "본래", "무엇", "가지", "은는", "이가", "때문", "스킴", "이후", "이전", "아래"]
        self.en_stop_words_list = en_stop_words_list

    def pre_processing(self, text) -> str:
        """ 텍스트 전처리 """
        # 한글,영어 아니면 전부 ' ' 로 치환
        result = re.sub(r'[^가-힣A-Za-z]', ' ', text)
        return result

    def ko_extract(self, text, top=150):
        ftext = self.pre_processing(text)
        tokens = filter(lambda s: len(s) > 1 and str(s).lower() not in self.kn_stop_words_list, self.mor.nouns(ftext))
        count = Counter(tokens)
        return count.most_common(top)

    def en_extract(self, text, top=150):
        ftext = self.pre_processing(text)
        tokens = filter(lambda s: len(s) > 3 and str(s).lower() not in self.en_stop_words_list,
                        nltk.word_tokenize(ftext))
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
