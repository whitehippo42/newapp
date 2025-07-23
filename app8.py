import streamlit as st
import calendar

st.markdown("<h1 style='text-align: center'> User Regi</h1>", unsafe_allow_html=True)

with st.form("form 3"):
	col1,col2 = st.columns(2)
	f_name = col1.text_input("first name")
	l_name = col1.text_input("last name")
	st.text_input("enter email")
	st.text_input("password", type="password")
	st.text_input("confirm password", type="password")
	day,month,year = st.columns(3)
	day.selectbox("day",range(1,32))
	month.selectbox("month",list(calendar.month_name)[1:])
	year.selectbox("year",range(1900,2025))
	s_state = st.form_submit_button("submit")
	if s_state:
		if f_name=='' or l_name=='':
			st.warning("please fill fields")
		else:
			st.success("submitted")