import streamlit as st

# ページ設定
st.set_page_config(
    page_title="🍨 ロネロネ星アイスアンケート",
    page_icon="🍦",
    layout="centered"
)

# やさしい背景CSS
st.markdown("""
<style>
.stApp {
    background: linear-gradient(180deg, #fff7fb, #f0f8ff);
}
h1, h2, h3 {
    color: #ff7aa2;
    text-align: center;
}
label {
    font-size: 18px;
}
</style>
""", unsafe_allow_html=True)

# タイトル
st.title("🐰 ロネロネ星 アイスアンケート 🍦")
st.write("うさぎのお姉さんのアイス屋さんへようこそ🌸")
st.write("よかったら答えてね✨")

st.divider()

# アンケート
name = st.text_input("① あなたの名前は？")
planet = st.text_input("② どこの星から来ましたか？")
food = st.text_input("③ 最近食べたおいしいものは？")
secret = st.text_area("④ あなたの秘密を教えてね…🤫")

# 送信ボタン
if st.button("🍦 送信する"):
    if name.strip() != "":
        st.success("ありがとう！アンケートを受け取りました🌟")
        st.write("### 📝 回答内容")
        st.write(f"**名前**：{name}")
        st.write(f"**星**：{planet}")
        st.write(f"**おいしいもの**：{food}")
        st.write(f"**秘密**：{secret}")
    else:
        st.warning("お名前は入れてね🐰")
