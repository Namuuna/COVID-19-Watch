import streamlit as st

from Views.intro import view as intro
from Views.dashboard import view as dashboard




if __name__ == '__main__':
    st.title("coronavirus - Watch")

    st.sidebar.title("Menu")

    menuOptions = ["Introduction","Graphs","Risk Rate"]

    menu = st.sidebar.selectbox("Features",menuOptions)

    views = {
    "Introduction"  : intro,
    "Graphs"        : dashboard
    }

    views[menu]()
