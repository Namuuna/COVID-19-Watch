import streamlit as st

def view():
    st.write("### Ways to Protect Yourself")
    st.image("https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fdatacdn.btimesonline.com%2Fdata%2Fimages%2Ffull%2F105605%2Fa-security-officer-in-a-protective-mask-checks-the-temperature-of-a-passenger-following-the-outbreak-of-a-new-coronavirus-at-an-expressway-toll-station-on-the-eve-of-the-chinese-lunar-new-year-celebrations-in-xianning.jpg&f=1&nofb=1",use_column_width=True)
    st.write('''
   The World Health Organization reccomends the following practices to protect yourself from contracting Coronavirus.

   * Wash your hands frequently and cough or sneeze into your elbow or a tissue to avoid the spread of germs
   * Avoid close contact with anyone that has a fever or cough
   * If you have fever, cough and difficulty breathing, see a doctor right away and share your travel history with them
   * Avoid travel to China, especially the Hubei province
   * Continue to protect yourself from other viruses, such as the flu, by getting vaccinated
    ''')
