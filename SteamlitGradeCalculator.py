import streamlit as st

st.title("Student Grade Calculator")
st.header("Enter Your Marks (out of 100)")

math    = st.number_input("Mathematics:", min_value=0.0, max_value=100.0)
english = st.number_input("English:",     min_value=0.0, max_value=100.0)
science = st.number_input("Science:",     min_value=0.0, max_value=100.0)

if st.button("Calculate Grade"):
    average = (math + english + science) / 3
    if   average >= 80: grade = "A"
    elif average >= 60: grade = "B"
    elif average >= 50: grade = "C"
    else:               grade = "F"

    st.divider()
    st.write(f"Average Score: {average:.2f}")
    if grade == "A":
        st.success(f"Grade: {grade} — Excellent!")
    elif grade in ["B","C"]:
        st.warning(f"Grade: {grade} — Keep it up!")
    else:
        st.error(f"Grade: {grade} — Failed!")
