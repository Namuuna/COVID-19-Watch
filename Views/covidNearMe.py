from math import sin, cos, sqrt, atan2, radians
import streamlit as st
import requests
import pandas as pd
import numpy as np


@st.cache
def retrieveData(url):
    data = requests.get(url)
    data = data.json()
    return data


def retrieveCoords(data):
    data = data["locations"]
    coords = []
    latest = []
    province = []
    for d in data:
        coords.append(d["coordinates"])
        latest.append(d["latest"])
        province.append(d["province"])
    return coords, latest, province


def heuristic(X, Y):
    # approximate radius of earth in km
    R = 6373.0
    lat1 = radians(float(X["lat"]))
    lon1 = radians(float(X["long"]))
    lat2 = radians(float(Y["lat"]))
    lon2 = radians(float(Y["long"]))
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = R * c
    return distance


def CovidNear(loc, coords, radius, latest, province):
    count = 0
    areas = []
    for i in range(len(coords)):
        coord = coords[i]
        Ncases = latest[i]
        area = province[i]
        if (heuristic(loc, coord)) <= radius:
            count += Ncases
            areas.append(area)
    return count, areas


def view():
    # Read Data
    url = "https://coronavirus-tracker-api.herokuapp.com/confirmed"
    rawData = retrieveData(url)
    coords, latest, province = retrieveCoords(rawData)

    # User Inputs
    lat = st.text_input("Latitude", value="39.9526")
    long = st.text_input("Longitude", value="75.1652")
    radius = st.slider("Radius (km)", min_value=1, max_value=1000, value=10)

    # Perform Calculation
    try:
        lat = float(lat)
        long = float(long)
        loc = {"lat": lat, "long": long}
        count, province = CovidNear(loc, coords, radius, latest, province)

        # Display Information
        st.info("Approximate confirmed cases nearby: " +
                str(count) + " within " + str(radius) + " km radius.")
        if (len(province) > 0):
            st.subheader("Infected Provinces:")
            p = pd.DataFrame(province, columns=["Province"])
            st.table(p)
            st.button("Share this")

    except:
        st.warning("Invalid Input!")
