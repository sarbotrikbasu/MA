import streamlit as st
import pandas as pd
import requests
import time
import config

# Page Config
st.set_page_config(
    page_title="MT5 Signal Dashboard",
    page_icon="📈",
    layout="wide"
)

# Custom CSS for modern styling
st.markdown("""
<style>
    .stApp {
        background-color: #0e1117;
    }
    .main-header {
        font-family: 'Inter', sans-serif;
        color: #ffffff;
        text-align: center;
        padding: 2rem 0;
    }
    .signal-table {
        margin: auto;
        border-collapse: collapse;
        width: 100%;
    }
</style>
""", unsafe_allow_html=True)

# Login System
def check_password():
    """Returns `True` if the user had a correct password."""

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if (
            st.session_state["username"] == "OrivisAlpha"
            and st.session_state["password"] == "Orivis"
        ):
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # don't store username + password
            del st.session_state["username"]
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        # First run, show inputs for username + password.
        st.header("Login")
        st.text_input("Username", key="username")
        st.text_input("Password", type="password", key="password")
        st.button("Login", on_click=password_entered)
        return False
    
    elif not st.session_state["password_correct"]:
        # Password not correct, show input + error.
        st.header("Login")
        st.text_input("Username", key="username")
        st.text_input("Password", type="password", key="password")
        st.button("Login", on_click=password_entered)
        st.error("😕 User not known or password incorrect")
        return False
        
    else:
        # Password correct.
        return True

if check_password():
    st.markdown("<h1 class='main-header'>MT5 SMA Logic Scanner</h1>", unsafe_allow_html=True)
    
    # Placeholder for table
    table_placeholder = st.empty()
    status_placeholder = st.empty()

    # Auto-refresh loop
    while True:
        try:
            # Fetch data from API
            response = requests.get("http://45.61.60.110:8001/signals")
            if response.status_code == 200:
                data = response.json()
                if data.get("status") == "success":
                    signals = data.get("data")
                    df = pd.DataFrame(signals)
                    
                    # Formatting for display
                    if not df.empty:
                        # Reorder columns as requested
                        cols = ["Symbol", "Timeframe", "SMA50", "SMA100", "SMA200", "Last Close", "Time"]
                        
                        # Apply styling
                        # Highlight 1s as Green, 0s as Neutral
                        def highlight_signal(val):
                            if val == 1:
                                return 'background-color: #1f7a1f; color: white'
                            elif val == -1:
                                return 'background-color: #7a1f1f; color: white'
                            return ''

                        styled_df = df[cols].style.applymap(highlight_signal, subset=["SMA50", "SMA100", "SMA200"])
                        
                        with table_placeholder.container():
                            st.write(styled_df)
                            st.caption(f"Last updated: {time.strftime('%H:%M:%S')}")
                    else:
                        table_placeholder.warning("No data received from API.")
                else:
                    table_placeholder.error(f"API Error: {data.get('message')}")
            else:
                 table_placeholder.error(f"Failed to connect to API. Status code: {response.status_code}")

        except requests.exceptions.ConnectionError:
            table_placeholder.error("Cannot connect to API. Is `api.py` running?")
        except Exception as e:
            table_placeholder.error(f"Error: {e}")
        
        # Sleep for refresh
        time.sleep(5) # Refresh every 5 seconds
        if False: break # Just to stop linter complaining about infinite loop
