# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 16:12:50 2026

@author: Administrator
"""

import numpy as np

def backtest(df):
    df["Signal"] = (df["EMA20"] > df["EMA50"]).astype(int)
    df["Returns"] = df["Close"].pct_change()
    df["Strategy"] = df["Signal"].shift(1) * df["Returns"]

    total = (1 + df["Strategy"]).cumprod().iloc[-1] - 1
    win_rate = (df["Strategy"] > 0).mean()

    return round(total*100,2), round(win_rate*100,2)