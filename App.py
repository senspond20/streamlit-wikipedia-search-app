import streamlit as st
import re
import time
from modules.wiki import WikiSearch, OutputFormat


def main():
    st.set_page_config(page_title="Wikipedia Search", page_icon=None, layout="centered", initial_sidebar_state="auto",
                       menu_items=None)
    st.title("Wikipedia Search :sunglasses:")
    option = st.selectbox("검색할 언어를 선택하세요", ("한국어(ko)", "영어(en)", "일본어(ja)", "중국어(zh)"))
    language = re.sub(r"[ㄱ-힣()]", "", option)
    keyword = st.text_input(label="검색 할 키워드를 입력하세요", value="")

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
                st.write(f"<h3>'{re_keyword}' in {option} 위키백과</h3>", unsafe_allow_html=True)
                st.write("link : " + page.fullurl)
                st.write("<h4>Summary</h4>", unsafe_allow_html=True)
                st.write(page.summary, unsafe_allow_html=True)

    st.image("https://images.unsplash.com/photo-1657256031790-e898b7b3f3eb?q=80&w=4032&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D")

    # footer
    with open("./footer.html", "r") as f:
        html = f.read()
        st.write(html, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
