
import streamlit as st
import pandas as pd
import time

st.set_page_config(layout="wide")
st.title("🚀 AutoTrade Pro Dashboard - 98% Accuracy")

# Header Metrics
col1, col2, col3 = st.columns(3)
col1.metric("📈 Portfolio Value", "₹127,460.52", "+₹1,250.00")
col2.metric("💼 Active Capital", "₹12,650", "88.3%")
col3.metric("📊 Active Trades", "24", "↗️")

# Chart Placeholder
st.subheader("📉 Live Trading Chart (Demo)")
st.line_chart(pd.DataFrame({
    "Price": [12000, 12100, 11950, 12250, 12300, 12450]
}))

# Active Trades Table
st.subheader("💹 Active Trades")
active_trades = pd.DataFrame({
    "Symbol": ["EURUSD", "GBPJPY", "USDJPY", "BALANCE"],
    "Type": ["BUY", "SELL", "BUY", "HOLD"],
    "P/L": ["₹+1,000", "₹+650", "₹+500", "₹12,650"]
})
st.table(active_trades)

# Market Watch
st.subheader("📊 Market Monitoring")
market_data = pd.DataFrame({
    "Symbol": ["EURUSD", "GBPUSD", "USDJPY", "AUDUSD"],
    "Price": [1.087, 1.276, 151.23, 0.667],
    "Change": ["+0.5%", "-0.3%", "+0.2%", "+0.1%"],
    "Signal": ["Buy", "Sell", "Buy", "Buy"]
})
st.dataframe(market_data, use_container_width=True)

# Trade Analytics
st.subheader("📈 Trade Analytics")
col1, col2 = st.columns(2)
col1.metric("Overall Accuracy", "98.1%")
col2.metric("Profit Factor", "3.45")

# Footer
st.markdown("---")
st.caption("© 2025 AutoTrade Pro | Built by Shashi")

# Auto-refresh
st_autorefresh = st.empty()
for i in range(3):
    st_autorefresh.text(f"⏳ Auto-refreshing in {3-i} seconds...")
    time.sleep(1)
