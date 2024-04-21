import streamlit as st

def find_biggest(num1, num2, num3):
  """Finds the biggest number among three."""
  return max(num1, num2, num3)

st.title("Find the Biggest Number")

num1 = st.number_input("Enter the first number:", key="num1")
num2 = st.number_input("Enter the second number:", key="num2")
num3 = st.number_input("Enter the third number:", key="num3")

if st.button("Find Biggest"):
  biggest_number = find_biggest(num1, num2, num3)
  st.write(f"The biggest number is: {biggest_number}")

  st.markdown("**Code prepared by 21f3002977_DaniyalIqbal**", unsafe_allow_html=False)

