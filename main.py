import streamlit as st

# Import Views
from Views.dashboard import view as dashboard
from Views.riskfactor import view as riskfactor
from Views.covidNearMe import view as covidNearMe


if __name__ == '__main__':
    st.title("coronavirus - Watch")

    st.sidebar.title("Menu")

    menuOptions = ["Dashboard", "Risk Factor", "COVID near me?"]

    menu = st.sidebar.selectbox("Features", menuOptions)

    views = {
        "Dashboard": dashboard,
        "Risk Factor": riskfactor,
        "COVID near me?": covidNearMe,
    }

    views[menu]()
