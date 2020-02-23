import requests
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
from datetime import datetime


@st.cache
def retrieveData(url):
    data = requests.get(url)
    data = data.json()
    return data


def createMap(data):
    data = data["locations"]
    mapData = []
    for d in data:
        if d["latest"] > 0:
            lat = float(d["coordinates"]["lat"])
            long = float(d["coordinates"]["long"])
            freq = int(d["latest"])
            mapData.append([lat, long, freq])
    mapData = pd.DataFrame(mapData, columns=["lat", "lon", "freq"])
    return mapData


def createLayer(data):
    layer = []

    freq = data["freq"]
    sizes, color, opacity = retrieveScales(freq)

    for i, _ in data.iterrows():
        row = data[i:i+1]
        layer.append({
            'type': 'ScatterplotLayer',
            'data': row,
            'radiusScale': 50,
            'radiusMinPixels': sizes[i],
            'getFillColor': color[i],
            'opacity': opacity[i],  
        })
    return layer


def retrieveScales(freq):
    size = []
    color = []
    opacity = []
    for f in freq:
        s = f / 50
        s = 5 if s < 5 else s
        s = 12 if s > 12 else s
        r = f / 20
        r = 150 if r < 150 else r
        o = f / 2000
        o = 0.5 if o < 0.5 else o
        opacity.append(o)
        color.append([r, 90, 80])
        size.append(s)
    return size, color, opacity


def plotMap(data):
    st.deck_gl_chart(
        viewport={'lat': 37.76, 'long': 110, 'zoom': 0},
        layers=createLayer(data))


def getPositiveCount(data):
    count = 0
    for date in data:
        count += int(data[date])
    return count


def createTimeData(data):
    time = {}
    timeData = []
    data = data["locations"]
    for d in data:
        for date in d["history"]:
            count = int(d["history"][date])
            if date in time:
                time[date] += count
            else:
                time[date] = count            

    for t in time:
        date = t
        cases = int(time[t])
        timeData.append([date, cases])

    timeData = pd.DataFrame(timeData, columns=["date", "cases"])
    timeData["date"] = pd.to_datetime(timeData["date"])
    timeData = timeData.sort_values(by=["date"])

    return timeData


def plotTimeData(data):
    c = alt.Chart(data,width=700).mark_circle().encode(
        x='date', y='cases')
    st.altair_chart(c)


def retrieveCountryData(data):
    data = data["locations"]
    countryList = {}
    countryData = []

    for d in data:
        country = d["country"]
        if country in countryList:
            countryList[country] += d["latest"]
        else:
            countryList[country] = d["latest"]

    for country in countryList:
        if int(countryList[country]) > 0:
            countryData.append([country, countryList[country]])
    countryData = pd.DataFrame(countryData, columns=["Country", "Total"])

    return countryData


def view():
    url = "https://coronavirus-tracker-api.herokuapp.com/all"
    rawData = retrieveData(url)

    getData = {
        "Confirmed": rawData["confirmed"],
        "Deaths": rawData["deaths"],
        "Recovered": rawData["recovered"]
    }

    latestConfirmed = getData["Confirmed"]["latest"]
    latestDeaths = getData["Deaths"]["latest"]
    latestRecovered = getData["Recovered"]["latest"]

    # Latest Numbers
    st.subheader("Latest Case Report")
    st.info("Confirmed - " + str(latestConfirmed))
    st.warning("Deaths - " + str(latestDeaths))
    st.success("Recovered - " + str(latestRecovered))
    st.markdown("<hr>", True)

    # Option Menu
    options = ["Confirmed", "Deaths", "Recovered"]
    selection = st.selectbox("Available Data", options)

    # Scatter plot for world map
    data = getData[selection]
    mapData = createMap(data)
    st.subheader("Map Distribution")
    plotMap(mapData)

    st.button("Share this")

    # Time series data
    st.subheader("Time Series Plot")
    timeData = createTimeData(data)
    plotTimeData(timeData)

    # Country Data
    st.subheader("Total Cases By Country")
    countryData = retrieveCountryData(data)
    st.table(countryData)
