import streamlit as st
import requests

css = """
<style>
    .stButton>button {
        color: white;
        background-color: #4CAF50;
        border-radius:20px;
        border:none;
        padding: 10px 24px;
        cursor: pointer;
        font-size: 18px;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
</style>
"""

st.markdown(css, unsafe_allow_html=True)
st.title('Big Data API Deployment')

# Endpoint
API_URL = "http://serving-api:8080"

# Form
with st.form("my_form"):
    seniority = st.number_input("Seniority")
    home = st.selectbox("Home", [0, 1])
    time = st.number_input("Time")
    age = st.number_input("Age")
    marital = st.selectbox("Marital", [0, 1])
    records = st.number_input("Records")
    job = st.selectbox("Job", [0, 1])
    expenses = st.number_input("Expenses")
    income = st.number_input("Income")
    assets = st.number_input("Assets")
    debt = st.number_input("Debt")
    amount = st.number_input("Amount")
    price = st.number_input("Price")

    submitted = st.form_submit_button("Submit")
    if submitted:
        datas = {
            "Seniority": seniority,
            "Home": home,
            "Time": time,
            "Age": age,
            "Marital": marital,
            "Records": records,
            "Job": job,
            "Expenses": expenses,
            "Income": income,
            "Assets": assets,
            "Debt": debt,
            "Amount": amount,
            "Price": price
        }
        response = requests.post(f"{API_URL}/predict", json=datas)

        if response.status_code == 200:
            results = response.json()
            st.write(f"Predictions: {results['predictions']}")
        else:
            st.write(f"Error: {response.status_code}")
