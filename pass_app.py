import streamlit as st

import joblib
import string
import random
import os
def load_model(model_file):
    loaded_model = joblib.load(open(os.path.join(model_file),"rb"))
    return loaded_model
pswd_vecotrizer = open("models/pswd_cv.pkl","rb")
pswd_cv = joblib.load(pswd_vecotrizer)

def get_key(val,my_dict):
    for key, value in my_dict.items():
        if val == value:
            return key
password_labels = {"weak":0, "average":1, "strong":2}
def password_classify():
    st.subheader("Classify Password")
    text = st.text_input("Enter Password", "Type Here")
    model_list = ["LR"]
    model_choice = st.selectbox("Select ML Model",model_list)
    if st.button("Classify"):
        vect_password = pswd_cv.transform([text]).toarray()
        if model_choice == 'LR':
            predictor = load_model("models/logit_pswd.pkl")
            prediction = predictor.predict(vect_password)
        final_result = get_key(prediction, password_labels)
        st.write(final_result)

def main():
    st.title("Password Strength Classifier")

if __name__ == "__main__":
    main()