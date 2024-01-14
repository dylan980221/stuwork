import streamlit as st
import numpy as np
import pandas as pd

st.title('ha')
st.write('# hahahahaha00')
st.write('## hahahahaha00')
st.info('12345')
a = np.array([1,2,3,4,5])
st.write(a)
st.table(a)

st.write('# ')
ch = st.checkbox('美食')
if ch:
    st.info('喜歡美食')
else:
    st.info('對美食沒興趣')

st.write('# ')
ch2 = st.checkbox('美食', 'key = a1')
if ch2:
    st.info('喜歡美食')
else:
    st.info('對美食沒興趣')


txt1 = ' '
chs = st.columns(3)
with chs[0]:
    c0=st.checkbox('飯', 'key = c0')
    if c0:
        st.write('白飯')
        txt1 +='要白飯'

with chs[1]:
    c1=st.checkbox('麵', 'key = c1')
    if c1:
        st.write('牛肉麵')
        txt1 += '要牛肉麵'

with chs[2]:
    c2=st.checkbox('湯', 'key = c2')
    if c2:
        st.write('貢丸湯')
        txt1 +="要一碗貢丸湯"
st.info(txt1)


gender = st.radio("請輸入:", ["男", "女", "不知"])
st.info(gender)

col1,col2=st.columns(2)
with col1:
    ra1 = st.number_input("請輸入要計算數字")
with col2:
    ra2 = st.number_input("請輸入要計算數字2", key='ra2')

ra3 = st.radio("請選擇符號", ['++','--','**','//'])

if ra3=='++':
    st.info(ra1+ra2)
elif ra3=='--':
    st.info(ra1-ra2)
elif ra3=='**':
    st.info(ra1*ra2)
elif ra3=='//':
    st.info(ra1/ra2)

num = st.slider('請調整到要的數字', 1.0, 20.0, step =0.5)
st.info(num)

city = st.selectbox('請選擇地方:',('台北', '台中', '台南'),index=1)
st.info(city)

file = st.file_uploader('請選擇上傳檔')
if file is not None:
    df = pd.read_csv(file)
    st.dataframe(df)