import streamlit as st
import pickle
import pandas as pd
from sklearn.compose import make_column_transformer
from sklearn.preprocessing import OrdinalEncoder
from PIL import Image

st.sidebar.title("Car Price Prediction Model")
html_temp = """
<div style="background-color:red;padding:10px">
<h2 style="color:white;text-align:center;">Streamlit ML Cloud App Project</h2>
</div>"""
st.markdown(html_temp, unsafe_allow_html=True)

# image=Image.open('car.jpg')
# st.image(image, use_column_width=True)

age = st.sidebar.selectbox("What is the age of your car?", (0, 1, 2, 3))
hp = st.sidebar.slider("What is the hp_kw of your car?", 40, 300, step=5)
km = st.sidebar.slider("What is the km of your car?", 0, 350000, step=1000)
gearing_type = st.sidebar.radio(
    'Select gear type', ('Automatic', 'Manual', 'Semi-automatic'))
car_model = st.sidebar.selectbox("Select model of your car", ('Audi A1', 'Audi A3', 'Opel Astra',
                                 'Opel Corsa', 'Opel Insignia', 'Renault Clio', 'Renault Duster', 'Renault Espace'))

my_model = pickle.load(open("rf_model", "rb"))

my_dict = {
    "age": age,
    "hp_kW": hp,
    "km": km,
    'Gearing_Type': gearing_type,
    "make_model": car_model
}

df_test = pd.DataFrame.from_dict([my_dict])

st.header("Your car specs:")
st.table(df_test)
col1, col2, col3 = st.columns(3)

with col1:
    st.write("")

with col2:
    if car_model == 'Audi A1' or car_model == 'Audi A3':
        image = Image.open('audi.jpg')
        st.image(image, use_column_width=False, width=150)
    if car_model == 'Opel Astra' or car_model == 'Opel Insignia' or car_model == 'Opel Corsa':
        image = Image.open('opel.jpg')
        st.image(image, use_column_width=False)
    if car_model == 'Renault Clio' or car_model == 'Renault Duster' or car_model == 'Renault Espace':
        image = Image.open('renault.jpg')
        st.image(image, use_column_width=False, width=150)

with col3:
    st.write("")

st.markdown(
    "<h2 style='text-align: center; color: black;'>Press [Predict] if your car's specs are correct.</h2>", unsafe_allow_html=True)

if st.button("Predict"):
    prediction = my_model.predict(df_test)
    st.success(
        f"The estimated price of your {car_model} is: € {int(prediction[0])}")
    st.markdown(f'<h1 style="color:red;font-size:24px; text-align:center">{"...Thanks for Using the Car Price Prediction Model..."}</h1>',
                unsafe_allow_html=True)
