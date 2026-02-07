
# MT5 Connection Settings
# IF you need specific login details, add them here. 
# Otherwise, MT5 will try to connect to the currently open terminal.
MT5_LOGIN = "413238944"
MT5_PASSWORD = "Sarbo1998@"
MT5_SERVER = "Exness-MT5Trial6"
MT5_PATH = "C:\\Program Files\\MetaTrader 5\\terminal64.exe"


# Trading Settings
SYMBOLS = [
    "EURUSDm", "XAUUSDm", "BTCUSDm", "ETHUSDm", 
    "GBPUSDm", "USDJPYm", "USDCHFm", "USDCADm", 
    "AUDUSDm", "NZDUSDm"
]
# Timeframes
TIMEFRAMES = {
    "5 min": mt5.TIMEFRAME_M5,
    "15 min": mt5.TIMEFRAME_M15,
    "1 hour": mt5.TIMEFRAME_H1
}

# Threshold for signal (0.0005)
SIGNAL_THRESHOLD = 0.0005
# Tolerance for floating point comparison
TOLERANCE = 1e-5

# Streamlit Credentials
ST_LOGIN = "OrivisAlpha"
ST_PASSWORD = "Orivis"
