import streamlit as st
import pandas as pd
import requests
import time

# ============================================
# CONFIG
# ============================================
API_URL = "http://45.61.60.110:8001/signals"

USERNAME = "OrivisAlpha"
PASSWORD = "Orivis"

st.set_page_config(page_title="Orivis Alpha Signals", layout="wide")


# ============================================
# LOGIN SYSTEM
# ============================================
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False


def login():

    st.title("Orivis Alpha Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):

        if username == USERNAME and password == PASSWORD:
            st.session_state.logged_in = True
            st.success("Login successful")
            st.rerun()
        else:
            st.error("Invalid credentials")


# ============================================
# FETCH DATA
# ============================================
def fetch_data():

    try:

        response = requests.get(API_URL, timeout=10)

        if response.status_code != 200:
            st.error("API Error")
            return pd.DataFrame()

        json_data = response.json()

        if json_data["status"] != "success":
            return pd.DataFrame()

        df = pd.DataFrame(json_data["data"])

        # Remove 'm' suffix
        df["Symbol"] = df["Symbol"].str.replace("m", "", regex=False)

        # Select only required columns
        df = df[[
            "Symbol",
            "Timeframe",
            "SMA50",
            "SMA100",
            "SMA200"
        ]]

        # Sort
        df = df.sort_values(["Symbol", "Timeframe"])

        return df

    except Exception as e:
        st.error(f"Connection Error: {e}")
        return pd.DataFrame()


# ============================================
# MAIN DASHBOARD
# ============================================
def dashboard():

    st.title("Orivis Alpha Signal Dashboard")

    col1, col2 = st.columns([1, 1])

    auto_refresh = col1.checkbox("Auto Refresh (5 sec)")
    refresh_btn = col2.button("Refresh Now")

    if auto_refresh:
        time.sleep(5)
        st.rerun()

    if refresh_btn:
        st.rerun()

    df = fetch_data()

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )


# ============================================
# APP FLOW
# ============================================
if not st.session_state.logged_in:
    login()
else:
    dashboard()
