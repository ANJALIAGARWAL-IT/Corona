import numpy as np
import pickle
import pandas as pd
import streamlit as st 

from PIL import Image
pickle_in = open("finalized_model.pkl","rb")
classifier=pickle.load(pickle_in)

def welcome():
    return "Welcome All"

def predict_class(Age,Fever,BodyPains,RunnyNose,Difficulty_in_Breath): 
    prediction=classifier.predict([[Age,Fever,BodyPains,RunnyNose,Difficulty_in_Breath]])
    return prediction



def main():
    st.title("CoronaVirus Predictior")
    html_temp = """
    <div style="background-color:green;padding:10px">
    <h2 style="color:white;text-align:center;">Corona Virus Predictor </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    Age = st.slider('Age',0,100)
    Fever = st.slider('Fever',0,110)
    BodyPains = st.text_input('BodyPains 0(NO)-1(YES)'," ")
    RunnyNose = st.text_input('RunnyNose 0(NO)-1(YES)'," ")
    Difficulty_in_Breath = st.text_input('Difficulty_in_Breath 0(NO)-1(YES)'," ")
    result=""
    if st.button("Predictor"):
        result=predict_class(int(Age),int(Fever),int(BodyPains),int(RunnyNose),int(Difficulty_in_Breath))
        if result==0:
            result="Great! You are not suffering from Corona Virus"
        else:
            result="Sorry! You are suffering from Corona Virus"
        
    st.success('The output is {}'.format(result))
    if st.button("About Me"):
        st.text("Anjali Agarwal")
        st.text("My Portfolio Profile - https://anjaliagarwal-it.github.io")
        st.text("My Linkedin Link - https://www.linkedin.com/in/anjaliagarwal98")
        st.text("My Github Link - https://github.com/ANJALIAGARWAL-IT/")

if __name__=='__main__':
    main()
    
