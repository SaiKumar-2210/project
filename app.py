from data import df,revenue_growth,net_income_growth,avg_metrics,yearly_totals
INTENTS={
    "revenue growth": revenue_growth,
    "net income growth": net_income_growth, 
    "avg metrics": avg_metrics,
    "yearly totals": yearly_totals
}
import streamlit as st
import pandas as pd
st.title("Financial Analysis Dashboard")
st.title("Chat Bot")
user_input = st.text_input("Ask a question about the financial data:")
if st.button("Submit"):
    for intent, response in INTENTS.items():
        if intent in user_input.lower():
            st.write(f"Response for '{intent}':")
            st.write(response())
            break
    else:
        st.write("Sorry, I don't understand that question. Please try again.")