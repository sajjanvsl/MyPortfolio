# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 16:13:02 2026

@author: Administrator
"""

def intraday_signal(df):
    df["RSI"] = ta.momentum.rsi(df["Close"], 14)
    df["VWAP"] = (df["Close"] * df["Volume"]).cumsum() / df["Volume"].cumsum()

    latest = df.iloc[-1]

    if latest["Close"] > latest["VWAP"] and latest["RSI"] > 55:
        return "BUY"
    elif latest["Close"] < latest["VWAP"] and latest["RSI"] < 45:
        return "SELL"
    else:
        return "NO TRADE"