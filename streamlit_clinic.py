import streamlit as st

from configs.simple import *

def main():
	st.title("Sistema Clinic")

	menu = ["Inicio", "Login"]
	choice = st.sidebar.selectbox("Menu", menu)

	if choice == "Inicio":
		st.subheader("Inicio")
	elif choice == "Login":
		st.subheader("Login")

main()