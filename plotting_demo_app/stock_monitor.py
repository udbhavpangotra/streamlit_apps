import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np


st.write(
    '''
    # Stock Tracker
    '''

)


stock_selection = st.selectbox('Please choose the stock you want to know about ',
                               ['GOOGL', 'MSFT', 'AMZN', 'TSLA'])


tickerSymbol = stock_selection

tickerData = yf.Ticker(tickerSymbol)

tickerDF = tickerData.history(
    period='max')

# ticker_info = tickerData.info

# short_name = ticker_info.shortName


st.line_chart(tickerDF.Close)
st.line_chart(tickerDF.Open)


st.write(

    '''
    This is my second attempt, I will be using the yfinance package to plot the opening and closing prices of apple and google stocks
    
    '''
)
