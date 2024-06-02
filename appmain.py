import streamlit as st
import langchainhelper as lch
st.title("Hotel Name and Place Recommender System")



user_input = st.text_input("Enter a country name")



if user_input:
    response= lch.generate_hotel_name_and_places(user_input)
    st.write("Hotel Name according to",user_input)
    st.header(response['hotel_name'].strip())
    st.write("**Hotel Places**")
    hotel_places= response['hotel_name'].strip().split(",")
    for hotel_place in hotel_places:
        st.write(hotel_place)
 
