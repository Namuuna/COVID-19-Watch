import requests
import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk


@st.cache
def retrieveData(url):
    data = requests.get(url)
    data = data.json()
    return data

def createMap(data):
    data = data["locations"]
    mapData = []
    for d in data:
        lat = float(d["coordinates"]["lat"])
        long = float(d["coordinates"]["long"])
        mapData.append([lat,long])
    mapData = pd.DataFrame(mapData,columns = ["lat","lon"])
    return mapData

def plotMap(data):
    st.deck_gl_chart(
        viewport = {
            'lat' : 37.76,
            'long': 110,
            'zoom': 0
            },
        layers=[{
                'type': 'ScatterplotLayer',
                'data': data,
                'radiusScale': 50,
                'radiusMinPixels': 5,
                'getFillColor': [248, 24, 148],
            }]
    )




url = "https://coronavirus-tracker-api.herokuapp.com/all"
data = retrieveData(url)
latest = data["latest"]
confirmed = data["confirmed"]
deaths = data["deaths"]
recovered = data["recovered"]

mapData = createMap(deaths)


def view():
    plotMap(mapData)
