# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 16:11:56 2026

@author: Administrator
"""

import yfinance as yf
import pandas as pd
import ta
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

def train_model(stock="RELIANCE.NS"):
    df = yf.download(stock, period="2y", progress=False)

    df["EMA20"] = ta.trend.ema_indicator(df["Close"], 20)
    df["EMA50"] = ta.trend.ema_indicator(df["Close"], 50)
    df["RSI"] = ta.momentum.rsi(df["Close"], 14)
    df["Return"] = df["Close"].pct_change().shift(-1)

    df["Target"] = (df["Return"] > 0).astype(int)

    df.dropna(inplace=True)

    X = df[["EMA20","EMA50","RSI"]]
    y = df["Target"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, shuffle=False)

    model = RandomForestClassifier(n_estimators=100)
    model.fit(X_train, y_train)

    accuracy = model.score(X_test, y_test)

    return model, accuracy