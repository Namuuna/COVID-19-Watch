import streamlit as st

def view():
    st.write("### Background Introduction")
    st.image("https://www.sciencenews.org/wp-content/uploads/2020/02/020720_ac-jl-ts_coronavirus_feat-1028x579.jpg",use_column_width=True)
    st.write('''
    The novel (new) coronavirus that was first detected in Wuhan City, Hubei Province, China. On February 11, 2020, the World Health Organization named the disease coronavirus disease 2019 (COVID-19).
    There are tens of thousands of cases of coronavirus disease in China with the virus reportedly spreading from the close contact between person-to-person, in particular through respiratory droplets from coughs and sneezes within a range of around 6 feet.

    The source of the virus is still unidentifed, but analysis of the genetric tree indicates that it originated in bats. However, it is unknown if the virus came directly from bats or it moved through an intermediary animal until it reached humans. Previously, SARS-CoV, another strain of the coronavirus, jumped from bats to civets and then infected humans and MERS-CoV jumped from bats to camels and then people.
    ''')
