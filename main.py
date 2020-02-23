import streamlit as st

# Import Views
from Views.dashboard import view as dashboard
from Views.riskfactor import view as riskfactor
from Views.covidNearMe import view as covidNearMe
from Views.about import view as about


if __name__ == '__main__':
    st.image("Data/Logo2.jpg", width = 80)
    st.title("Coronavirus - Watch")

    st.sidebar.title("Menu")
    menuOptions = ["Dashboard", "Risk Factor", "COVID near me?", "About"]
    menu = st.sidebar.selectbox("Features", menuOptions)

    views = {
        "Dashboard"     : dashboard,
        "Risk Factor"   : riskfactor,
        "COVID near me?": covidNearMe,
        "About"         : about
    }

    views[menu]()
