import streamlit as st
import pandas as pd
import numpy as np


def view():
    st.write("Below is the equation that is used for calculating: ")
    st.image("Data/calculationFlow.PNG",width=700)
    st.write("Economic Resilience: ")
    st.write("Economic resilience is the ability of a country to do something about a shock, either directly (health related) or in economic terms, such as the ability to use fiscal or monetary stimuli. It could also include governance, and here we include health governance.Thus we measure economic resilience as:")
    st.write("1. fiscal balance/GDP (%)")
    st.write("2. current account balance/GDP (%)")
    st.write("3. foreign currency reserves in months of imports")
    st.write("4. external debt/GDP (%)")
    st.write("5. expenditure on health/GDP (%)")
    st.write("6. health care access and quality index")
    st.write("A country may also be exposed to China even if does not trade with China but when it trades with a third country that does trade with China. This means that a country that is more open to trade (including tourism) and investment in general will be affected more.")
    st.write("1. exports of goods and services/GDP (%)")
    st.write("2. FDI inflows/GDP (%)")
    st.write("3. personal remittances received/GDP (%)")
    st.write("4. migrants/population (%)")
    st.write("5. international tourism receipts/total exports (%).")
    st.write("References: https://set.odi.org/wp-content/uploads/2020/02/Economic-Vulnerability.pdf")
