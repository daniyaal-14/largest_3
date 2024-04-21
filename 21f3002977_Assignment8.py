opimport streamlit as st

def largest(n1, n2, n3):
  """Finds the biggest number among three."""
  return max(n1, n2, n3)

st.title("Largest of 3 Number")

n1 = st.number_input("Enter the first number:", key="n1")
n2 = st.number_input("Enter the second number:", key="n2")
n3 = st.number_input("Enter the third number:", key="n3")

if st.button("Find Biggest"):
  biggest_number = largest(n1, n2, n3)
  st.header(f"The biggest number among provided 3 is: {biggest_number}")

"***Devloped by 21f3002977_DaniyalIqbal***"

