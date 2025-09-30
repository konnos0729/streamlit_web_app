import streamlit as st


with st.form(key='profile_form'):
    name = st.text_input('名前')
    address = st.text_input('住所')

    age_category = st.selectbox(
            '年齢層',
            ('子ども(18才未満)', '大人(18才以上)', '高齢者(65才以上)'))
    
    hobby = st.multiselect(
        '趣味',
        ('スポーツ', '読書', 'プログラミング','アニメ・映画','釣り','料理'))

    submit_btn = st.form_submit_button('送信')
    cancel_btn = st.form_submit_button('キャンセル')
    if submit_btn:
        st.text(f'ようこそ！{name}さん')
        st.text(f'年齢層：{age_category}です。')
        st.text(f'趣味：{", ".join(hobby)}です。')
