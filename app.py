# Libraries
import pickle as pk
import pandas as pd
import numpy as np
import streamlit as st
from PIL import Image


# Load the model
model = pk.load(open('pakwheels.pkl', 'rb'))
general = pk.load(open('dic_general.pkl','rb'))
special = pk.load(open('dic.pkl','rb'))

# Title
st.title('Used Cars Price Predictor (Trained on Dataset of upto Oct 2021')

# Take Inputs
make = st.selectbox('Make', general['brands'])
vehicle = st.selectbox('Vehicle', list(special[make].keys()))
variant = st.selectbox('Variant', list(special[make][vehicle].keys()))
registered = st.selectbox('Registered City', general['registration'])
color = st.selectbox('Colour', (special[make][vehicle][variant]['colours']))
transmission = st.selectbox('Transmission', general['transmission'])
engine_type = st.selectbox('Engine', general['engine_type'])
vehicle_model = st.selectbox('Model', (sorted(special[make][vehicle][variant]['models'])))
hp = st.selectbox('Engine CC', (sorted(special[make][vehicle][variant]['cc'])))
mileage = st.text_input("Enter Mileage").lower()






# make = st.text_input("Enter Brand").lower()
# vehicle = st.text_input("Enter Vehicle Name").lower()
# variant = st.text_input("Enter Variant").lower()
# vehicle_model = st.text_input("Enter Model").lower()
# color = st.text_input("Enter Colour").lower()
# mileage = st.text_input("Enter Mileage").lower()
# registered = st.text_input("Enter Registration City").lower()
# hp = st.text_input("Enter Horse Power (CC)").lower()
# transmission = st.text_input("Enter Transmission Type (Automatic/Manual)").lower()
# engine_type = st.text_input("Enter Engine Type (Petrol/Diesel)").lower()


# Pass Input to loaded model
if st.button('Predict'):
    vehicle_model = int(vehicle_model)
    hp = int(hp)

    if variant == 'Unknown':
        variant = ''

    if make.isnumeric():
        st.write('Maker cannot be numbers. It should be english word')
        
    if vehicle.isnumeric():
        st.write('Vehicle cannot be numbers. It should start with english character')
        
    if variant.isnumeric():
        st.write('Vehicle cannot be numbers. It should start with english character')
        
    if type(vehicle_model) != int:
        st.write('Model cannot be english word. It should be some number')
        
    if color.isnumeric():
        st.write('Colour cannot be number. It should be name of Colour in english')
        
    if mileage.isnumeric() != True:
        st.write('Milage cannot be english word. It should be some number')
        
    if registered.isnumeric():
        st.write('Registration city cannot be number. It should be name of city in english')
        
    if type(hp) != int:
        st.write('Horse Power cannot be english word. It should be number')
        
    if transmission.isnumeric():
        st.write('Transmission cannot be number. It should either be Manual or automatic')
        
    if engine_type.isnumeric():
        st.write('Engine type cannot be number. It should be english word')

    else:    
        inp = [[vehicle_model, mileage, registered, color, hp, make, vehicle, variant, transmission, engine_type]] 
        out = model.predict(inp)
        st.success('The Predicted Price of Vehicle is Rs: {} Lakhs'. format(np.round(out[0],3)))

