import streamlit as st
import re
import time
from modules.wiki_search import WikiSearch, OutputFormat
from modules.word_extraction import WordExtraction
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from wordcloud import WordCloud
from modules.components.lang_selector import get_value, LanguageSelectbox

def main():
    st.set_page_config(page_title="Wikipedia Search", page_icon=None, layout="centered", initial_sidebar_state="auto",
                       menu_items=None)
    # Streamlit의 description은 앱 GitHub 저장소의 README에서 설명을 가져온다..

    st.title("Wikipedia Search :sunglasses:")
    option = LanguageSelectbox()
    language = get_value(option)

    keyword = st.text_input(label="검색 할 키워드를 입력하세요", value="")

    img_show = True
    if st.button(type="primary", label="검색"):
        if str(keyword).strip() == "":
            st.warning('키워드를 입력해주세요', icon="⚠️")
        else:
            st.write("")
            wiki = WikiSearch(language, OutputFormat.HTML)
            re_keyword, page = wiki.search(keyword)
            with st.spinner(f"{option} 위키백과에서 '{re_keyword}' 검색 중입니다..."):
                time.sleep(3)

            if not page.exists():
                st.error(f"{option} 위키백과에서 '{re_keyword}' 검색된 결과가 없어요...", icon="⚠️")
            else:
                st.write(f"<h3><span style='color:royalblue'>'{re_keyword}'</span> in {option} 위키백과</h3>", unsafe_allow_html=True)
                st.write("link : " + page.fullurl)
                st.write("<h4>Summary</h4>", unsafe_allow_html=True)
                st.info("위키백과의 검색결과를 요약합니다")
                st.write(page.summary, unsafe_allow_html=True)

                we = WordExtraction()

                tokens = None
                if language == 'ko':
                    st.spinner(f"키워드 추출 중입니다...")
                    tokens = we.ko_extract(page.text)
                elif language == 'en':
                    st.spinner(f"키워드 추출 중입니다...")
                    tokens = we.en_extract(page.text)
                else:
                    st.info("한국어/영어 위키백과를 제외한 키워드 추출은 지원되지 않습니다.")

                if tokens:
                    st.write(f"<h4>키워드 추출</h4>", unsafe_allow_html=True)
                    st.info("위키백과의 본문에서 형태소 분석기로 키워드(최대 150개)를 추출합니다")
                    wc = WordCloud(
                        font_path="./SeoulNamsanvert.ttf",
                        background_color="white",
                        width=1000,
                        height=1000,
                        max_words=100,
                        max_font_size=300)
                    wc = wc.generate_from_frequencies(dict(tokens))

                    fig = plt.figure()
                    plt.imshow(wc, interpolation='bilinear')
                    plt.axis('off')
                    st.pyplot(fig)
                    nsp = np.array(tokens)
                    st.dataframe(pd.DataFrame(data= { "keyword" : nsp[:, 0], "count" : nsp[:,1]}))
                    img_show = False    # 하단 이미지 안보이게

    if img_show:
        st.image("https://images.unsplash.com/photo-1657256031790-e898b7b3f3eb?q=80&w=4032&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D")


    # footer
    with open("./footer.html", "r") as f:
        html = f.read()
        st.write(html, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
