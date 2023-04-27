import streamlit as st
from confirm_button_hack import cache_on_button_press
import catboost
import pickle
import pandas as pd

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
    model = model.load_model('/Users/seonghyunpark/python_boostcamp2/project-serving/trained_model_20230426_133927.cbm')

    uploaded_file = st.file_uploader("Upload your pickle file", type=['pkl'])

    if uploaded_file : 
        #데이터 로드 부분
        _data = uploaded_file.getvalue()
        df = pickle.loads(_data)
        
        #데이터 전처리
        X_test = df.drop(['rating'], axis=1)

        #데이터 일부 보여주기 
        st.write(df.head())

        #예측 & 기존 데이터 채우기
        st.write("Predicting.....")
        y_test = model.predict(X_test)
        df['rating'] = y_test 

        #결과 보여주기
        st.write(df)
        st.write("Done!")
        
        #다운로드 파일을 만들기 위해 convert_df, 이때 cache_data를 이용해 매번 로드할 필요 없도록 함
        file_for_download = convert_df(df)

        #다운로드 부분
        st.download_button(
            label = "Download result for csv", 
            data = file_for_download,
            file_name = 'result.csv'
            )

@st.cache_data
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')        

main()
                    
# @cache_on_button_press('Authenticate')
# def authenticate(password, userid) ->bool:
#     return (password == root_password) & (userid == root_userid)

# userid = st.text_input('userid', type="password")
# password = st.text_input('password', type="password")

# if authenticate(password, userid):
#     st.success('You are authenticated!')
#     main()
# else:
#     st.error('The password is invalid.')