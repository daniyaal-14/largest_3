import streamlit as st
def largest(n1, n2, n3):
    return max(n1, n2, n3)
def main():
    st.title("Largest Of 3 Numbers")

    n1 = st.number_input("Enter your 1st number:", step=1)
    n2 = st.number_input("Enter the 2nd number:", step=1)
    n3 = st.number_input("Enter the 3rd number:", step=1)

    if st.button("Get Largest"):
        maximum = largest(n1, n2, n3)
        st.success(f"The Biggest number is: {maximum}")

if __name__ == "__main__":
    main()
