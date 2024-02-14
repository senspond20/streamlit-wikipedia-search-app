import streamlit as st
# import re 

lang_options = {
    "한국어" : "ko",
    "영어" : "en",
    "일본어" : "ja",
    "중국어" : "zh"
}

def LanguageSelectbox(key=None):
    """streamlit selectbox component"""
    return st.selectbox("검색할 언어를 선택하세요", tuple(lang_options.keys()), key=key)

def get_value(option="한국어"):
    """get value from lang_options dict"""
    return lang_options[str(option)]