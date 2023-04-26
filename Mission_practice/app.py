import streamlit as st
from confirm_button_hack import cache_on_button_press
st.write()

# SETTING PAGE CONFIG TO WIDE MODE
st.set_page_config(layout="wide")
root_password = 'password'
root_userid = 'Seonghyun'

#TODO 모델 불러오기
#TODO 모델을 학습하기 위한 데이터도 함께 불러오기 

def main():
    st.title("Book Rating Prediction")



@cache_on_button_press('Authenticate')
def authenticate(password, userid) ->bool:
    return (password == root_password) & (userid == root_userid)

userid = st.text_input('userid', type="password")
password = st.text_input('password', type="password")

if authenticate(password, userid):
    st.success('You are authenticated!')
    main()
else:
    st.error('The password is invalid.')