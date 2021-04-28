"""
Benny's Burgers
"""
import streamlit as st

BEEF = 5.25
BEYOND = 6.25
CHEESE = 0.50
AVOCADO = 0.75
CHILI = 1.25

price = 0.0
toppingsPrice = [CHEESE, CHILI, AVOCADO]

st.title("Welcome to Benny's Burgers")
st.image("burgers.jpg")

meat = st.radio("Please select your choice of protein:", ["Beef", "Beyond Beef"])
st.write("Meat = ", meat)               # st.text does not work here

box = st.radio("Do you like to have toppings?", ["Yes","No"])

if box == "Yes":
    toppings = st.multiselect("Please select the toppings: ",["Cheese", "Chili", "Avocado"])
    st.write(toppings)

if meat == 'Beef':
    beefPrice = BEEF
    price += BEEF
else:
    beefPrice = BEYOND
    price += BEYOND

if "Cheese" in toppings:
    price += CHEESE
if "Chili" in toppings:
    price += CHILI
if "Avocado" in toppings:
    price += AVOCADO

st.header("Order Summary")
st.text("="*15 + "Order Summary" + "="*20)
st.text(f"Beef: {meat:10s}\t\t\t${beefPrice:6.2f}")
if box == "Yes":
    st.text(f'Toppings')
    for i in range(len(toppings)):
       st.text(f"Topping 1: {toppings[i]:10s}\t\t\t${toppingsPrice[i]:6.2f}")
st.text(f"{'Total:':20s}\t\t\t${price:>6,.2f}")
st.text("-"*48)

st.balloons()
