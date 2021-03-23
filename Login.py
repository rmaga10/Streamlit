import streamlit as st
import numpy as np
import pandas as pd
import sqlite3


# Login 
conn = sqlite3.connect('database.db')
c = conn.cursor()

def create_usertable():
	c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT UNIQUE,password TEXT)')
	
		
def add_userdata(username,password):
		c.execute(' INSERT INTO userstable(username,password) VALUES (?,?)',(username,password))
		conn.commit()

def login_user(username,password):
	c.execute('SELECT * FROM userstable WHERE username =? AND password = ?',(username,password))
	data = c.fetchall()
	return data

def view_all_users():
	c.execute('SELECT * FROM userstable')
	data =c.fetchall()
	return data



# Home
st.title("My first app")

menu = ["Home", "Login", "SignUp"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Home":
	st.subheader("Home")

elif choice == "Login":
	st.subheader("Login Section")

	username = st.sidebar.text_input("Usuário")
	password = st.sidebar.text_input("password", type='password')
	if st.sidebar.button("Login"):
		#if password == 'admin':
		create_usertable()
		result = login_user(username,password)
		if result:


			st.success("Logado como {}".format(username))

			df = pd.DataFrame({
			  'first column': [1, 2, 3, 4],
			  'second column': [10, 20, 30, 40],
			  'third': [0.02,0.045,0.5897,0.89785]
			})

			df


			user_result = view_all_users()
			clean_db = pd. DataFrame(user_result,columns=["username","password"])
			st.dataframe(clean_db)

			chart_data = pd.DataFrame(
			     np.random.randn(20, 3),
			     columns=['a', 'b', 'c'])

			st.line_chart(chart_data)

			map_data = pd.DataFrame(
			    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
			    columns=['lat', 'lon'])

			st.map(map_data)

			if st.checkbox('Show dataframe'):
			    chart_data = pd.DataFrame(
			       np.random.randn(20, 3),
			       columns=['a', 'b', 'c'])

			    chart_data


			option = st.sidebar.selectbox(
			    'Which number do you like best?',
			     df['first column'])

			'You selected:', option

			left_column, right_column = st.beta_columns(2)
			pressed = left_column.button('Press me?')
			if pressed:
			    right_column.write("Woohoo!")

			expander = st.beta_expander("FAQ")
			expander.write("Here you could put in some really, really long explanations...")

		else:
			st.warning("Incorrect Username/password")


# Login
elif choice == "SignUp":
	st.subheader("Criar nova conta")
	new_user = st.text_input("Username")
	new_password = st.text_input("Password", type="password")

	if st.button("SignUp"):
		create_usertable()
		try:
			add_userdata(new_user, new_password)
			st.success("Criado com sucesso")
			st.info("Ir para Login")
		except:
			st.info("Usuário já existe")
			



