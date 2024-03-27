import streamlit as st


st.sidebar.selectbox('Select', ['US','UK','DE','FR'])
st.sidebar.slider('Temperature')

clicked = st.button("Click Me")

if clicked:
	st.write(':ghost:' * 3)

st.divider()

prompt = st.chat_input("Say something")
if prompt:
    st.write(f"User: {prompt}")