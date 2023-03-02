import streamlit as st
import numpy as np
import pickle
import pandas as pd

###loading the trained model
loaded_model = pickle.load(open('random_model.sav' , 'rb'))

st.title('Airline Satisfaction :airplane:')
seatclass = st.selectbox('Select the type of seat' , ['Economy' , 'Economy +' , 'Business'])
if seatclass == "Economy":
    seatclass = 0
elif seatclass == 'Economy +':
    seatclass = 1
elif seatclass == 'Business':
    seatclass = 2
traveltype = st.selectbox('Select the type of Travel' ,['Personal' , 'Business'])
if traveltype == "Personal":
    traveltype = 0
elif traveltype == 'Business':
    traveltype = 1
onlineboardingexp =  st.select_slider('Please rate Online Boarding experience',[1,2,3,4,5])
wifiexp =  st.select_slider('Please rate Inflight wifi experience',[1,2,3,4,5])
entertainmentexp = st.select_slider('Please rate Inflight entertainment experience',[1,2,3,4,5])
seatcomfort = st.select_slider('Please rate seating comfort',[1,2,3,4,5])
legroom = st.select_slider('Please rate legroom space',[1,2,3,4,5])
fightdistance = st.slider('Flight distance form origin to destination' , min_value=40 , max_value=5000)
onboardservice = st.select_slider('Please rate Online Boarding service',[1,2,3,4,5])
cleanliness = st.select_slider('Please rate Cleanliness',[1,2,3,4,5])
easeofbooking = st.select_slider('Please rate Ease of booking',[1,2,3,4,5])
inflightservice = st.select_slider('Please rate Inflight services',[1,2,3,4,5])
bagage = st.select_slider('Please rate Baggage Handling',[1,2,3,4,5])
age = st.slider('How old are you ?',min_value=14 , max_value = 100)

def predict():
    row = np.asarray([onlineboardingexp,wifiexp,seatclass,traveltype,entertainmentexp,seatcomfort,legroom,fightdistance,onboardservice,cleanliness,easeofbooking,inflightservice,age,bagage])
    row = row.reshape(1,-1)
    prediction = loaded_model.predict(row)

    if prediction == 1:
        st.success('The customer is Satisfied with the service:thumbsup:')
    else:
        st.success('The customer is Not Satisfied with the service:thumbsdown:')

st.button('Predict' , on_click =predict )