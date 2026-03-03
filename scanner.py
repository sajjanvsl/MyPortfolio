# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 16:11:14 2026

@author: Administrator
"""

import yfinance as yf
import pandas as pd
import ta

nifty50 = [
"RELIANCE.NS","TCS.NS","HDFCBANK.NS","INFY.NS","ICICIBANK.NS",
"SBIN.NS","ITC.NS","LT.NS","KOTAKBANK.NS","HINDUNILVR.NS"
]

def scan():
    results = []

    for stock in nifty50:
        df = yf.download(stock, period="6mo", progress=False)

        df["EMA20"] = ta.trend.ema_indicator(df["Close"], 20)
        df["EMA50"] = ta.trend.ema_indicator(df["Close"], 50)
        df["RSI"] = ta.momentum.rsi(df["Close"], 14)
        df["ATR"] = ta.volatility.average_true_range(df["High"], df["Low"], df["Close"])
        df["AvgVol"] = df["Volume"].rolling(20).mean()

        latest = df.iloc[-1]

        score = 0
        if latest["EMA20"] > latest["EMA50"]: score += 25
        if 45 < latest["RSI"] < 65: score += 20
        if latest["Volume"] > 1.2 * latest["AvgVol"]: score += 20
        if latest["Close"] > df["High"].rolling(20).max().iloc[-2]: score += 15
        if latest["ATR"] > df["ATR"].mean(): score += 10
        score += 10  # RS simplified

        results.append((stock, score))

    return sorted(results, key=lambda x: x[1], reverse=True)