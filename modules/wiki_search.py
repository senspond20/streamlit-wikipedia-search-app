import wikipediaapi
import re

class OutputFormat():
    WIKI = 1
    HTML = 2


class WikiSearch():
    wiki = None

    def __init__(self, language: str, format: OutputFormat):
        """
        :param language: "ko"/"en" ..
        :param format: WIKI (텍스트 형식)/ HTML
        """
        params = {
            "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
            "language": language,
            "extract_format": format
        }
        self.wiki = wikipediaapi.Wikipedia(**params)


    def search(self, keyword: str):
        """
        :param keyword: 검색할 키워드
        :return: page
        """
        # 한글,영문,숫자 외 이상한 문자 제거
        re_keyword = re.sub(r"[^ㄱ-힝a-zA-Z0-9]", "", keyword)

        return re_keyword, self.wiki.page(re_keyword)

if __name__ == "__main__":
    wiki_ko = WikiSearch("ko", OutputFormat.WIKI)
    re_keyword, page = wiki_ko.search("인공지능")
    print(page.title)
    # print(page.summary)
    print(page.text)
