# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 16:13:13 2026

@author: Administrator
"""

import pandas as pd

def portfolio_summary(trades):
    df = pd.DataFrame(trades)
    total_profit = df["Profit"].sum()
    win_rate = (df["Profit"] > 0).mean() * 100
    return total_profit, win_rate