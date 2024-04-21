import streamlit as st
def find_max(num1, num2, num3):
    return max(num1, num2, num3)
def main():
    st.title("Maximum Number Finder")

    num1 = st.number_input("Enter the first number:", step=1)
    num2 = st.number_input("Enter the second number:", step=1)
    num3 = st.number_input("Enter the third number:", step=1)

    if st.button("Find Maximum"):
        maximum = find_max(num1, num2, num3)
        st.success(f"The maximum number is: {maximum}")

if __name__ == "__main__":
    main()
