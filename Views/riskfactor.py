import streamlit as st
import pandas as pd
import numpy as np


@st.cache
def retrieveData(url):
    data = pd.read_csv(url)
    return data


def createLayer(data):
    layer = []

    riskFactor = data["Risk"]
    colors, sizes = retrieveRiskScales(riskFactor)

    for i, d in data.iterrows():
        row = data[i:i+1]
        layer.append({
            'type': 'ScatterplotLayer',
            'data': row,
            'radiusScale': 50,
            'radiusMinPixels': sizes[i],
            'getFillColor': colors[i]
        })
    return layer


def plotMap(data):
    st.deck_gl_chart(
        viewport={
            'lat': 37.76,
            'long': 110,
            'zoom': 0
        },
        layers=createLayer(data)
    )


def retrieveRiskScales(risk):
    color = []
    size = []

    for R in risk:
        r = int(300 * R)
        g = int(50 * (1/R))
        b = int(10 * (1/R))
        a = 1.5 * R
        color.append([r, g, b])
        size.append(R*15)
    return color, size

def inputDescription():
    image = 'Data/graph.PNG'
    st.image("Data/graph.png", width = 650)
    st.write("Above map shows countries with the greatest exposure to a China slowdown directly or indirectly. It was calculated based on five indicators:" )
    st.write("Exports of goods and services/GDP (%)")
    st.write("FDI inflows/GDP (%)")
    st.write("Personal remittances received/GDP (%)")
    st.write("Migrants/population (%)") 
    st.write("International tourism receipts/total exports (%).")
    st.write("Each indicator is given an equal weight of 0.20 with the highest possible sub-index score of 1.")

def view():
    file = "Data/RiskData.csv"
    rawData = retrieveData(file)

    # st.table(rawData)
    st.subheader("Risk Factor Map")
    plotMap(rawData)
    inputDescription()
