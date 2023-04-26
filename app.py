import streamlit as st
from confirm_button_hack import cache_on_button_press
import catboost
st.write()

# SETTING PAGE CONFIG TO WIDE MODE
st.set_page_config(layout="wide")
root_password = 'password'
root_userid = 'Seonghyun'

#TODO 모델 불러오기
#TODO 모델을 학습하기 위한 데이터도 함께 불러오기 

def main():
    st.title("Book Rating Prediction using CatBoost")
    model = catboost.CatBoostRegressor()
    #기존에 저장해 둔 모델만을 불러오는 것이기 때문에, Batch service의 개념과 같다.
    model.load_model('20230426_093711')

    uploaded_file = st.file_uploader("Upload your pickle file", type=['pkl'])

    if uploaded_file : 
        _data = uploaded_file.getvalue()
        print(_data)


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