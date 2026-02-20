import streamlit as st
import pandas as pd
import numpy as np

# Displaying text content
st.title("My First Streamlit App")
st.write("Hello, Prathmesh")
st.text("Let's start!")

# Creating charts using pandas and numpy
df = pd.DataFrame(
    np.random.randn(10, 2),
    columns=['A', 'B']
)

st.line_chart(df)
st.bar_chart(df)

# Sidebar, image and video
st.sidebar.title("Navigation")

st.image("https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png")
st.caption("Google Logo")

st.video("https://www.youtube.com/watch?v=uP7uhlDrlD4&list=RDYyepU5ztLf4&index=3")
#file uplode(csv)
st.title("CSV File Uploader App")

# Upload file
uploaded_file = st.file_uploader("Upload a CSV file", type='csv')

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.write("Here is your data:")
    st.dataframe(data)

# Taking user input
name = st.text_input("Enter name:")

if st.button("Welcome"):
    st.write(f"Welcome {name} 🚀")
#textdown and markdown formating
st.title("Text vs Markdown Example")

st.text("This is plain text.")
st.text("No bold, no color, no formatting.")


st.text_input(" What is Your Name?")
st.text_area("write something.....")
st.number_input("pick a number", min_value=0, max_value=100)
st.slider("Choose a range", 0, 100)
st.selectbox("Select a fruit", ["Apple", "Banana", "Mango"])
st.multiselect("Choose Toppings", ["Cheese", "Tomato", "Olives"])
st.radio("Pick One", ["Option A", "Option B"])
st.checkbox("I agree to the terms")


#matplotlib integration
import matplotlib.pyplot as plt
x = [1,2,3,4]
y = [10,20,25,30]

plt.plot(x, y)
plt.title("Simple Plot")
plt.show()